# Getting Started with PERLA

Welcome to PERLA! This tutorial will guide you through your first steps with the Perovskite Solar Cells Living Archive. By the end of this guide, you'll understand how to access and explore the database.

## What You'll Learn

- How to access the PERLA database through NOMAD
- Basic navigation and search functionality
- Understanding the data structure and available parameters
- Your first data query and visualization

## Prerequisites

- Basic understanding of perovskite solar cells
- Familiarity with web browsers (no programming required for basic access)
- Optional: Python knowledge for API access

## Step 1: Accessing the PERLA Database

The PERLA database is hosted on the NOMAD platform and accessible through a web interface.

1. **Open your web browser** and navigate to:
   ```
   https://nomad-lab.eu/prod/v1/staging/gui/search/perovskite-solar-cells-database
   ```

2. **Explore the interface**: You'll see a search interface with various filters and visualization options.

3. **No registration required**: The database is freely accessible without creating an account.

## Step 2: Understanding the Data Structure

The database is organized around cell entries. Each cell from a paper leads to a new entry.
The entries contain different amounts of information, based on what could be extracted.


## Step 3: Basic Search and Filtering

### Simple Search
1. Use the search bar to find entries by: free text search or searching in particular fields.

### Advanced Filtering
1. **Efficiency Range**: Filter devices by PCE values
2. **Publication Date**: Focus on recent or historical data
3. **Device Type**: Filter by architecture (n-i-p vs p-i-n)
4. **Materials**: Search by specific perovskite compositions

### Example Search
Try searching for high-efficiency inverted devices:
- Set efficiency filter: > 20%
- Device structure: p-i-n
- Publication date: Last 2 years

## Step 4: Exploring Visualizations

PERLA provides interactive visualizations:

1. **Efficiency Trends**: See performance evolution over time
2. **Architecture Distribution**: Compare device types
3. **Composition Analysis**: Explore material trends
4. **Stability Correlations**: Understand performance-stability relationships

## Step 5: Exporting Data

For further analysis, you can export data in multiple formats:

1. API query for downloading the dataset
2. Export of selected entries (as raw files or processes entities)

## Next Steps

### For Beginners
- Explore the [Case Studies](../notebooks/query-perovskite-database.ipynb) for guided analysis examples
- Try different search combinations to understand data coverage
- Review the [Data Schema](../reference/schema.md) for complete parameter definitions

### For Advanced Users
- Learn [API access](../how_to/api_query.md) for programmatic data retrieval
- Set up [local extraction](../how_to/local_extraction.md) for your own papers
- Contribute to the database through [data validation](../how_to/contribute_data.md)


## Summary

You've learned how to:
- ✅ Access the PERLA database through NOMAD
- ✅ Navigate the search interface and apply filters
- ✅ Understand the hierarchical data structure
- ✅ Export data for your own analysis
- ✅ Find additional resources for advanced usage

Ready for more? Continue with [Your First Query](first_query.md) to learn about programmatic access, or dive into our [Case Studies](../notebooks/query-perovskite-database.ipynb) for real research examples.