#!/bin/bash
# Script to prepare documentation by copying notebooks from perovskite plugin
# This script is used in CI/CD pipelines where symlinks may not work

set -e  # Exit on error

# Define paths
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PERLA_DIR="$(dirname "$SCRIPT_DIR")"
NOTEBOOKS_TARGET="$PERLA_DIR/docs/notebooks"

# Subpath within the perovskite plugin
PEROVSKITE_SUBPATH="src/perovskite_solar_cell_database/example_uploads/perla_notebooks"

# Check multiple possible locations for the perovskite plugin
# Location 1: Sibling directory (local dev with monorepo structure)
NOTEBOOKS_SOURCE_LOCAL="$PERLA_DIR/../nomad-perovskite-solar-cells-database/$PEROVSKITE_SUBPATH"
# Location 2: Inside workspace root (CI checkout structure)
NOTEBOOKS_SOURCE_CI="$PERLA_DIR/nomad-perovskite-solar-cells-database/$PEROVSKITE_SUBPATH"

echo "Preparing documentation notebooks..."

# Determine which source exists
if [ -d "$NOTEBOOKS_SOURCE_LOCAL" ]; then
    NOTEBOOKS_SOURCE="$NOTEBOOKS_SOURCE_LOCAL"
    echo "Found notebooks in sibling directory (local dev structure)"
elif [ -d "$NOTEBOOKS_SOURCE_CI" ]; then
    NOTEBOOKS_SOURCE="$NOTEBOOKS_SOURCE_CI"
    echo "Found notebooks in workspace subdirectory (CI structure)"
else
    echo "ERROR: Source notebooks directory not found!"
    echo "Checked locations:"
    echo "  1. $NOTEBOOKS_SOURCE_LOCAL"
    echo "  2. $NOTEBOOKS_SOURCE_CI"
    echo "Please ensure nomad-perovskite-solar-cells-database is available."
    exit 1
fi

echo "Source: $NOTEBOOKS_SOURCE"
echo "Target: $NOTEBOOKS_TARGET"

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
