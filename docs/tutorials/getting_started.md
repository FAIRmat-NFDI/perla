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
1. Use the search bar to find entries by: free text search or searching in particular fields. If you type in the search bar, you can select between free text search across the entire entries or specific search methods on fields. Clicking on the questionmark reveals details.

![Example of search](../assets/gifs/search.gif)

### Example Search
Try searching for high-efficiency inverted devices:
- Set efficiency filter: > 20%
- Absorber: FAPbI3

## Step 4: Exploring Visualizations

The NOMAD frontend allows to interactively explore data via visualizations. You can interact with the existing ones or easily add novel ones.

![Visualization](../assets/gifs/visualization.gif)

## Step 5: Exporting Data

For further analysis, you can export data in multiple formats:

1. API query for downloading the dataset
2. Export of selected entries (as raw files or processes entities)

![Export](../assets/gifs/export.gif)


## Summary

You've learned how to:
- ✅ Access the PERLA database through NOMAD
- ✅ Navigate the search interface and apply filters
- ✅ Understand the hierarchical data structure
- ✅ Export data for your own analysis

Ready for more?  Dive into our [Case Studies](../notebooks/query-perovskite-database.ipynb) for real research examples.