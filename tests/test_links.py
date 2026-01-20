"""
Test suite to validate documentation links and notebook paths.
Ensures notebooks from perovskite plugin are accessible and internal links resolve.
"""

import os
import re
from pathlib import Path
import pytest
import yaml


# Get the perla package directory
PERLA_DIR = Path(__file__).parent.parent
DOCS_DIR = PERLA_DIR / "docs"
MKDOCS_CONFIG = PERLA_DIR / "mkdocs.yml"


def test_mkdocs_config_exists():
    """Verify mkdocs.yml configuration file exists."""
    assert MKDOCS_CONFIG.exists(), f"mkdocs.yml not found at {MKDOCS_CONFIG}"


def test_notebooks_symlink_or_directory_exists():
    """Verify docs/notebooks exists (either as symlink or directory)."""
    notebooks_path = DOCS_DIR / "notebooks"
    assert notebooks_path.exists(), f"Notebooks path not found at {notebooks_path}"
    
    # Check if it's a symlink
    if notebooks_path.is_symlink():
        target = notebooks_path.resolve()
        assert target.exists(), f"Symlink target does not exist: {target}"
        print(f"✓ Notebooks symlink points to: {target}")
    else:
        print(f"✓ Notebooks directory exists at: {notebooks_path}")


def test_notebooks_source_accessible():
    """Verify the source notebooks in perovskite plugin are accessible."""
    # Resolve the actual source path
    source_path = PERLA_DIR.parent / "nomad-perovskite-solar-cells-database" / "src" / "perovskite_solar_cell_database" / "example_uploads" / "perla_notebooks"
    
    assert source_path.exists(), (
        f"Source notebooks directory not found: {source_path}\n"
        f"Ensure nomad-perovskite-solar-cells-database is available as a sibling package."
    )
    
    # Check for expected notebooks
    notebooks = list(source_path.glob("*.ipynb"))
    assert len(notebooks) > 0, f"No notebooks found in {source_path}"
    print(f"✓ Found {len(notebooks)} notebooks in source directory")


def test_all_referenced_notebooks_exist():
    """Verify all notebooks referenced in mkdocs.yml actually exist."""
    with open(MKDOCS_CONFIG, 'r') as f:
        config = yaml.safe_load(f)
    
    # Extract all notebook references from nav
    notebook_refs = []
    
    def extract_notebooks(nav_item):
        """Recursively extract notebook paths from nav structure."""
        if isinstance(nav_item, dict):
            for key, value in nav_item.items():
                if isinstance(value, str) and value.endswith('.ipynb'):
                    notebook_refs.append(value)
                elif isinstance(value, (list, dict)):
                    extract_notebooks(value)
        elif isinstance(nav_item, list):
            for item in nav_item:
                extract_notebooks(item)
    
    if 'nav' in config:
        extract_notebooks(config['nav'])
    
    print(f"\nChecking {len(notebook_refs)} notebook references...")
    
    missing_notebooks = []
    for notebook_ref in notebook_refs:
        # Remove 'notebooks/' prefix if present for checking
        notebook_path = DOCS_DIR / notebook_ref
        if not notebook_path.exists():
            missing_notebooks.append(notebook_ref)
        else:
            print(f"✓ {notebook_ref}")
    
    assert not missing_notebooks, (
        f"Missing notebooks referenced in mkdocs.yml:\n" +
        "\n".join(f"  - {nb}" for nb in missing_notebooks)
    )


def test_markdown_internal_links():
    """Verify internal links in markdown files resolve correctly."""
    markdown_files = list(DOCS_DIR.rglob("*.md"))
    
    # Pattern to match markdown links: [text](path)
    link_pattern = re.compile(r'\[([^\]]+)\]\(([^\)]+)\)')
    
    # Known missing pages that are expected (work in progress)
    expected_missing = {
        'tutorials/first_query.md',
        'how_to/nomad_access.md',
        'how_to/api_query.md',
        'how_to/local_extraction.md',
        'how_to/automation_bot.md',
        'how_to/contribute_data.md',
        'how_to/contribute_to_perla.md',
        'explanation/schema_mapping.md',
        'reference/api.md',
        'reference/schema.md',
    }
    
    broken_links = []
    
    for md_file in markdown_files:
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        matches = link_pattern.findall(content)
        
        for link_text, link_path in matches:
            # Skip external URLs
            if link_path.startswith(('http://', 'https://', 'mailto:', '#')):
                continue
            
            # Skip anchor-only links
            if link_path.startswith('#'):
                continue
            
            # Skip placeholders
            if 'PLACEHOLDER' in link_path:
                continue
            
            # Resolve relative links
            if not link_path.startswith('/'):
                # Relative to the markdown file
                target_path = (md_file.parent / link_path).resolve()
                # Get relative path from docs for checking expected_missing
                try:
                    relative_to_docs = target_path.relative_to(DOCS_DIR)
                except ValueError:
                    relative_to_docs = None
            else:
                # Absolute from docs root
                target_path = (DOCS_DIR / link_path.lstrip('/')).resolve()
                relative_to_docs = Path(link_path.lstrip('/'))
            
            # Check if target exists
            if not target_path.exists():
                # Check if it's an expected missing page
                if relative_to_docs and str(relative_to_docs) in expected_missing:
                    print(f"⚠ Expected missing page: {link_path}")
                    continue
                
                # Check if it's an anchor link (ending with #something)
                if '#' in link_path:
                    base_path = link_path.split('#')[0]
                    if base_path:
                        base_target = (md_file.parent / base_path).resolve()
                        if base_target.exists():
                            # Base file exists, anchor may be valid
                            continue
                
                broken_links.append({
                    'file': md_file.relative_to(PERLA_DIR),
                    'link_text': link_text,
                    'link_path': link_path,
                    'resolved_path': target_path
                })
    
    if broken_links:
        error_msg = "Broken internal links found:\n"
        for link in broken_links:
            error_msg += f"\n  In {link['file']}:"
            error_msg += f"\n    Link text: {link['link_text']}"
            error_msg += f"\n    Link path: {link['link_path']}"
            error_msg += f"\n    Resolved to (missing): {link['resolved_path']}\n"
        
        pytest.fail(error_msg)


def test_required_notebooks_present():
    """Verify critical notebooks are present."""
    required_notebooks = [
        "query-perovskite-database.ipynb",
        "performance-evolution.ipynb",
        "bandgap-evolution.ipynb",
        "architecture-evolution.ipynb",
        "diversity_analysis.ipynb",
        "crabnet-perovskite-bandgap-prediction.ipynb",
        "ml-distribution-shift-case-study.ipynb",
        "perovscribe-analysis.ipynb",
        "perovskite-paperbot-plot.ipynb",
    ]
    
    notebooks_dir = DOCS_DIR / "notebooks"
    missing = []
    
    for notebook in required_notebooks:
        notebook_path = notebooks_dir / notebook
        if not notebook_path.exists():
            missing.append(notebook)
        else:
            print(f"✓ {notebook}")
    
    assert not missing, f"Required notebooks missing: {', '.join(missing)}"


if __name__ == "__main__":
    # Run tests with verbose output
    pytest.main([__file__, "-v"])
