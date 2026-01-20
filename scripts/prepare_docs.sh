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

# List of specific notebooks to copy (without underscores and backup copies)
NOTEBOOKS=(
    "query-perovskite-database.ipynb"
    "performance-evolution.ipynb"
    "bandgap-evolution.ipynb"
    "architecture-evolution.ipynb"
    "diversity-analysis.ipynb"
    "crabnet-perovskite-bandgap-prediction.ipynb"
    "ml-distribution-shift-case-study.ipynb"
    "perovscribe-analysis.ipynb"
    "perovskite-paperbot-plot.ipynb"
)

# Copy specific notebooks
echo "Copying notebooks..."
for notebook in "${NOTEBOOKS[@]}"; do
    if [ -f "$NOTEBOOKS_SOURCE/$notebook" ]; then
        cp "$NOTEBOOKS_SOURCE/$notebook" "$NOTEBOOKS_TARGET/"
        echo "  ✓ $notebook"
    else
        echo "  ✗ WARNING: $notebook not found in source"
    fi
done

# Copy supporting Python files (plotly_theme.py, etc.)
if [ -f "$NOTEBOOKS_SOURCE/plotly_theme.py" ]; then
    cp "$NOTEBOOKS_SOURCE/plotly_theme.py" "$NOTEBOOKS_TARGET/"
    echo "  ✓ plotly_theme.py"
fi

echo "Documentation notebooks prepared successfully!"
echo "Notebooks copied: ${#NOTEBOOKS[@]}"
