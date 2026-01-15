# Getting Started with PERLA

Welcome to PERLA! This tutorial will guide you through your first steps with the Perovskite Extraction & Research Living Archive. By the end of this guide, you'll understand how to access and explore the database.

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

PERLA organizes data hierarchically:

```
Publication → Device → Measurements
```

### Key Parameters Available

**Device Architecture**
- Device structure (n-i-p, p-i-n)
- Layer materials and thicknesses
- Substrate information

**Perovskite Composition**
- Chemical formula
- Cation and anion compositions
- Processing conditions

**Performance Metrics**
- Power conversion efficiency (PCE)
- Open-circuit voltage (Voc)
- Short-circuit current density (Jsc)
- Fill factor (FF)

**Stability Data**
- Operational stability
- Storage stability
- Environmental testing conditions

## Step 3: Basic Search and Filtering

### Simple Search
1. Use the search bar to find entries by:
   - Author names
   - Publication titles
   - Material keywords (e.g., "FA", "perovskite", "inverted")

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

1. **JSON**: Machine-readable format for programming
2. **CSV**: Spreadsheet-compatible format
3. **Excel**: Direct import into Excel or similar tools

## Next Steps

### For Beginners
- Explore the [Case Studies](../notebooks/query-perovskite-database.ipynb) for guided analysis examples
- Try different search combinations to understand data coverage
- Review the [Data Schema](../reference/schema.md) for complete parameter definitions

### For Advanced Users
- Learn [API access](../how_to/api_query.md) for programmatic data retrieval
- Set up [local extraction](../how_to/local_extraction.md) for your own papers
- Contribute to the database through [data validation](../how_to/contribute_data.md)

## Troubleshooting

### Common Issues

**Slow Loading**
- The database is continuously updated; initial loading may take a moment
- Try refreshing the page if search results don't appear

**No Results Found**
- Check your filter settings - they may be too restrictive
- Try broader search terms
- Clear all filters and start with basic searches

**Visualization Not Loading**
- Ensure JavaScript is enabled in your browser
- Try a different browser if issues persist
- Some visualizations require larger datasets to display properly

## Getting Help

- **Documentation**: Explore other sections of this documentation
- **GitHub Issues**: Report problems or ask questions
- **Community**: Connect with other PERLA users

## Summary

You've learned how to:
- ✅ Access the PERLA database through NOMAD
- ✅ Navigate the search interface and apply filters
- ✅ Understand the hierarchical data structure
- ✅ Export data for your own analysis
- ✅ Find additional resources for advanced usage

Ready for more? Continue with [Your First Query](first_query.md) to learn about programmatic access, or dive into our [Case Studies](../notebooks/query-perovskite-database.ipynb) for real research examples.