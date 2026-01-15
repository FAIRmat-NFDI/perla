# Your First Query

This tutorial teaches you how to programmatically access PERLA data using the NOMAD API. You'll learn to write Python code that queries the database and processes the results.

## What You'll Learn

- How to use the NOMAD API to access PERLA data
- Basic Python setup for data queries
- Filtering and retrieving specific datasets
- Processing and analyzing query results

## Prerequisites

- Python 3.7 or higher
- Basic Python programming knowledge
- Completed the [Getting Started](getting_started.md) tutorial

## Setup

### Install Required Packages

```bash
pip install requests pandas matplotlib seaborn jupyter
```

### Import Libraries

```python
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json
from datetime import datetime
```

## Step 1: Understanding the NOMAD API

The PERLA database is accessible through NOMAD's REST API. The base URL for queries is:

```python
BASE_URL = "https://nomad-lab.eu/prod/v1/api/v1/entries"
```

### Basic Query Structure

NOMAD queries use a JSON structure with filters and pagination:

```python
query = {
    "query": {
        "and": [
            # Your filters go here
        ]
    },
    "pagination": {
        "page_size": 100
    }
}
```

## Step 2: Your First Query

Let's start with a simple query to get recent perovskite solar cell entries:

```python
def query_perla_data(filters=None, page_size=100):
    """
    Query the PERLA database through NOMAD API
    """
    url = "https://nomad-lab.eu/prod/v1/api/v1/entries"
    
    # Base query for perovskite solar cells
    query = {
        "query": {
            "and": [
                {
                    "nested": {
                        "path": "data",
                        "query": {
                            "exists": {
                                "field": "data.solar_cell"
                            }
                        }
                    }
                }
            ]
        },
        "pagination": {
            "page_size": page_size
        }
    }
    
    # Add custom filters if provided
    if filters:
        query["query"]["and"].extend(filters)
    
    response = requests.post(url, json=query)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

# Execute your first query
data = query_perla_data(page_size=50)
print(f"Found {data['pagination']['total']} entries")
```

## Step 3: Adding Filters

### Filter by Efficiency Range

Let's query for high-efficiency devices (>20% PCE):

```python
# Filter for high-efficiency devices
efficiency_filter = [
    {
        "nested": {
            "path": "data.solar_cell.device.efficiency",
            "query": {
                "range": {
                    "data.solar_cell.device.efficiency": {
                        "gte": 0.20
                    }
                }
            }
        }
    }
]

high_eff_data = query_perla_data(filters=efficiency_filter)
print(f"Found {high_eff_data['pagination']['total']} high-efficiency entries")
```

### Filter by Publication Date

Query for recent publications (last 2 years):

```python
from datetime import datetime, timedelta

# Calculate date 2 years ago
two_years_ago = datetime.now() - timedelta(days=730)
date_string = two_years_ago.strftime("%Y-%m-%d")

date_filter = [
    {
        "range": {
            "upload_create_time": {
                "gte": date_string
            }
        }
    }
]

recent_data = query_perla_data(filters=date_filter)
print(f"Found {recent_data['pagination']['total']} recent entries")
```

### Combine Multiple Filters

Combine efficiency and date filters:

```python
combined_filters = efficiency_filter + date_filter
combined_data = query_perla_data(filters=combined_filters)
print(f"Found {combined_data['pagination']['total']} high-efficiency recent entries")
```

## Step 4: Processing Query Results

### Extract Key Parameters

```python
def extract_device_parameters(entries):
    """
    Extract key parameters from NOMAD entries
    """
    devices = []
    
    for entry in entries:
        try:
            # Extract basic information
            device = {
                'entry_id': entry.get('entry_id'),
                'upload_create_time': entry.get('upload_create_time'),
                'authors': entry.get('authors', []),
            }
            
            # Extract solar cell data if available
            if 'data' in entry and 'solar_cell' in entry['data']:
                solar_cell = entry['data']['solar_cell']
                
                if 'device' in solar_cell:
                    device_data = solar_cell['device']
                    device.update({
                        'efficiency': device_data.get('efficiency'),
                        'voc': device_data.get('voc'),
                        'jsc': device_data.get('jsc'),
                        'fill_factor': device_data.get('fill_factor'),
                        'device_area': device_data.get('device_area'),
                        'architecture': device_data.get('architecture')
                    })
                
                if 'perovskite' in solar_cell:
                    perovskite_data = solar_cell['perovskite']
                    device.update({
                        'composition': perovskite_data.get('composition'),
                        'bandgap': perovskite_data.get('bandgap')
                    })
            
            devices.append(device)
            
        except Exception as e:
            print(f"Error processing entry {entry.get('entry_id', 'unknown')}: {e}")
            continue
    
    return devices

# Process the query results
if combined_data and 'data' in combined_data:
    devices = extract_device_parameters(combined_data['data'])
    df = pd.DataFrame(devices)
    
    print(f"Processed {len(devices)} devices")
    print("\nDataFrame columns:", df.columns.tolist())
    print("\nFirst few entries:")
    print(df.head())
```

## Step 5: Basic Analysis

### Efficiency Distribution

```python
# Plot efficiency distribution
plt.figure(figsize=(10, 6))
df['efficiency'].dropna().hist(bins=20, alpha=0.7)
plt.xlabel('Power Conversion Efficiency')
plt.ylabel('Number of Devices')
plt.title('Distribution of Device Efficiencies')
plt.grid(True, alpha=0.3)
plt.show()
```

### Efficiency vs. Voltage

```python
# Scatter plot of efficiency vs. open-circuit voltage
plt.figure(figsize=(10, 6))
plt.scatter(df['voc'], df['efficiency'], alpha=0.6)
plt.xlabel('Open-circuit Voltage (V)')
plt.ylabel('Power Conversion Efficiency')
plt.title('Efficiency vs. Open-circuit Voltage')
plt.grid(True, alpha=0.3)
plt.show()
```

### Architecture Comparison

```python
# Compare architectures if data is available
if 'architecture' in df.columns and df['architecture'].notna().any():
    arch_counts = df['architecture'].value_counts()
    
    plt.figure(figsize=(8, 6))
    arch_counts.plot(kind='bar')
    plt.xlabel('Device Architecture')
    plt.ylabel('Number of Devices')
    plt.title('Distribution of Device Architectures')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
```

## Step 6: Advanced Querying

### Pagination for Large Datasets

```python
def query_all_pages(filters=None, max_entries=1000):
    """
    Query multiple pages to get more data
    """
    all_entries = []
    page = 0
    page_size = 100
    
    while len(all_entries) < max_entries:
        # Update pagination
        query = {
            "query": {
                "and": [
                    {
                        "nested": {
                            "path": "data",
                            "query": {
                                "exists": {
                                    "field": "data.solar_cell"
                                }
                            }
                        }
                    }
                ]
            },
            "pagination": {
                "page_size": page_size,
                "page": page
            }
        }
        
        if filters:
            query["query"]["and"].extend(filters)
        
        response = requests.post(BASE_URL, json=query)
        
        if response.status_code == 200:
            data = response.json()
            entries = data.get('data', [])
            
            if not entries:  # No more data
                break
                
            all_entries.extend(entries)
            print(f"Retrieved page {page + 1}, total entries: {len(all_entries)}")
            page += 1
        else:
            print(f"Error on page {page}: {response.status_code}")
            break
    
    return all_entries[:max_entries]

# Get more data
large_dataset = query_all_pages(max_entries=500)
print(f"Retrieved {len(large_dataset)} total entries")
```

## Troubleshooting

### Common Issues

**Empty Results**
```python
# Check if query returned data
if data is None or 'data' not in data:
    print("No data returned. Check your query and filters.")
```

**API Rate Limits**
```python
import time

# Add delays between requests for large queries
time.sleep(0.1)  # 100ms delay
```

**Missing Parameters**
```python
# Check for missing data
missing_efficiency = df['efficiency'].isna().sum()
print(f"Entries missing efficiency data: {missing_efficiency}")
```

## Next Steps

### Explore Case Studies
- [Performance Evolution Analysis](../notebooks/performance-evolution.ipynb)
- [Architecture Trends](../notebooks/architecture-evolution.ipynb)
- [ML Predictions](../notebooks/crabnet-perovskite-bandgap-prediction.ipynb)

### Advanced Topics
- [Local Extraction Setup](../how_to/local_extraction.md)
- [Contributing Data](../how_to/contribute_data.md)
- [API Reference](../reference/api.md)

## Summary

You've learned how to:
- ✅ Set up Python for PERLA data access
- ✅ Write basic queries using the NOMAD API
- ✅ Apply filters for specific datasets
- ✅ Process and analyze query results
- ✅ Create visualizations from the data
- ✅ Handle pagination for larger datasets

You're now ready to explore the full power of PERLA's programmatic interface and conduct your own analyses!