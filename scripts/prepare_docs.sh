#!/bin/bash
# Script to prepare documentation by copying notebooks from perovskite plugin
# This script is used in CI/CD pipelines where symlinks may not work

set -e  # Exit on error

# Define paths
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PERLA_DIR="$(dirname "$SCRIPT_DIR")"
NOTEBOOKS_SOURCE="$PERLA_DIR/../nomad-perovskite-solar-cells-database/src/perovskite_solar_cell_database/example_uploads/perla_notebooks"
NOTEBOOKS_TARGET="$PERLA_DIR/docs/notebooks"

echo "Preparing documentation notebooks..."
echo "Source: $NOTEBOOKS_SOURCE"
echo "Target: $NOTEBOOKS_TARGET"

# Check if source directory exists
if [ ! -d "$NOTEBOOKS_SOURCE" ]; then
    echo "ERROR: Source notebooks directory not found: $NOTEBOOKS_SOURCE"
    echo "Please ensure nomad-perovskite-solar-cells-database is available as a sibling directory."
    exit 1
fi

# Remove existing notebooks directory (could be symlink or directory)
if [ -e "$NOTEBOOKS_TARGET" ]; then
    echo "Removing existing notebooks directory/symlink..."
    rm -rf "$NOTEBOOKS_TARGET"
fi

# Create target directory
mkdir -p "$NOTEBOOKS_TARGET"

# Copy notebooks and supporting files
echo "Copying notebooks..."
cp -r "$NOTEBOOKS_SOURCE"/*.ipynb "$NOTEBOOKS_TARGET/" || {
    echo "ERROR: Failed to copy notebooks"
    exit 1
}

# Copy supporting Python files (plotly_theme.py, etc.)
if [ -f "$NOTEBOOKS_SOURCE/plotly_theme.py" ]; then
    cp "$NOTEBOOKS_SOURCE/plotly_theme.py" "$NOTEBOOKS_TARGET/"
fi

# Copy parquet data file if it exists
if [ -f "$NOTEBOOKS_SOURCE/perovskite_solar_cell_database.parquet" ]; then
    echo "Copying data file..."
    cp "$NOTEBOOKS_SOURCE/perovskite_solar_cell_database.parquet" "$NOTEBOOKS_TARGET/"
fi

echo "Documentation notebooks prepared successfully!"
echo "Notebooks copied: $(ls -1 "$NOTEBOOKS_TARGET"/*.ipynb | wc -l)"
