"""
Test suite to validate documentation links and notebook paths.
Ensures notebooks from perovskite plugin are accessible and internal links resolve.
"""

import re
from pathlib import Path

import pytest
import yaml

# Get the perla package directory
PERLA_DIR = Path(__file__).parent.parent
DOCS_DIR = PERLA_DIR / 'docs'
MKDOCS_CONFIG = PERLA_DIR / 'mkdocs.yml'


def test_mkdocs_config_exists():
    """Verify mkdocs.yml configuration file exists."""
    assert MKDOCS_CONFIG.exists(), f'mkdocs.yml not found at {MKDOCS_CONFIG}'


def test_notebooks_symlink_or_directory_exists():
    """Verify docs/notebooks exists (either as symlink or directory)."""
    notebooks_path = DOCS_DIR / 'notebooks'
    assert notebooks_path.exists(), f'Notebooks path not found at {notebooks_path}'

    # Check if it's a symlink
    if notebooks_path.is_symlink():
        target = notebooks_path.resolve()
        assert target.exists(), f'Symlink target does not exist: {target}'
        print(f'✓ Notebooks symlink points to: {target}')
    else:
        print(f'✓ Notebooks directory exists at: {notebooks_path}')


def test_notebooks_source_accessible():
    """Verify the source notebooks in perovskite plugin are accessible."""
    # Subpath within the perovskite plugin
    perovskite_subpath = (
        'src'
        / Path('perovskite_solar_cell_database')
        / 'example_uploads'
        / 'perla_notebooks'
    )

    # Check multiple possible locations for the perovskite plugin
    # Location 1: Sibling directory (local dev with monorepo structure)
    source_path_local = (
        PERLA_DIR.parent / 'nomad-perovskite-solar-cells-database' / perovskite_subpath
    )
    # Location 2: Inside workspace root (CI checkout structure)
    source_path_ci = (
        PERLA_DIR / 'nomad-perovskite-solar-cells-database' / perovskite_subpath
    )

    # Determine which source exists
    if source_path_local.exists():
        source_path = source_path_local
        print('✓ Found notebooks in sibling directory (local dev structure)')
    elif source_path_ci.exists():
        source_path = source_path_ci
        print('✓ Found notebooks in workspace subdirectory (CI structure)')
    else:
        pytest.fail(
            f'Source notebooks directory not found!\n'
            f'Checked locations:\n'
            f'  1. {source_path_local}\n'
            f'  2. {source_path_ci}\n'
            f'Ensure nomad-perovskite-solar-cells-database is available.'
        )

    # Check for expected notebooks
    notebooks = list(source_path.glob('*.ipynb'))
    assert len(notebooks) > 0, f'No notebooks found in {source_path}'
    print(f'✓ Found {len(notebooks)} notebooks in source directory')


def test_all_referenced_notebooks_exist():
    """Verify all notebooks referenced in mkdocs.yml actually exist."""
    with open(MKDOCS_CONFIG) as f:
        # Use unsafe_load to handle !!python/name: tags in mkdocs.yml
        # safe_load can't parse Python object references used by mkdocs plugins
        config = yaml.unsafe_load(f)

    # Extract all notebook references from nav
    notebook_refs = []

    def extract_notebooks(nav_item):
        """Recursively extract notebook paths from nav structure."""
        if isinstance(nav_item, dict):
            for key, value in nav_item.items():
                if isinstance(value, str) and value.endswith('.ipynb'):
                    notebook_refs.append(value)
                elif isinstance(value, list | dict):
                    extract_notebooks(value)
        elif isinstance(nav_item, list):
            for item in nav_item:
                extract_notebooks(item)

    if 'nav' in config:
        extract_notebooks(config['nav'])

    print(f'\nChecking {len(notebook_refs)} notebook references...')

    missing_notebooks = []
    for notebook_ref in notebook_refs:
        # Remove 'notebooks/' prefix if present for checking
        notebook_path = DOCS_DIR / notebook_ref
        if not notebook_path.exists():
            missing_notebooks.append(notebook_ref)
        else:
            print(f'✓ {notebook_ref}')

    assert not missing_notebooks, (
        'Missing notebooks referenced in mkdocs.yml:\n'
        + '\n'.join(f'  - {nb}' for nb in missing_notebooks)
    )


def _should_skip_link(link_path: str) -> bool:
    """Check if a link should be skipped during validation."""
    return (
        link_path.startswith(('http://', 'https://', 'mailto:', '#'))
        or 'PLACEHOLDER' in link_path
    )


def _resolve_link_path(link_path: str, md_file: Path) -> tuple[Path, Path | None]:
    """Resolve a link path to its target and relative path from docs."""
    if not link_path.startswith('/'):
        target_path = (md_file.parent / link_path).resolve()
        try:
            relative_to_docs = target_path.relative_to(DOCS_DIR)
        except ValueError:
            relative_to_docs = None
    else:
        target_path = (DOCS_DIR / link_path.lstrip('/')).resolve()
        relative_to_docs = Path(link_path.lstrip('/'))
    return target_path, relative_to_docs


def _is_valid_anchor_link(link_path: str, md_file: Path) -> bool:
    """Check if an anchor link has a valid base file."""
    if '#' not in link_path:
        return False
    base_path = link_path.split('#')[0]
    if not base_path:
        return False
    base_target = (md_file.parent / base_path).resolve()
    return base_target.exists()


def test_markdown_internal_links():
    """Verify internal links in markdown files resolve correctly."""
    markdown_files = list(DOCS_DIR.rglob('*.md'))
    link_pattern = re.compile(r'\[([^\]]+)\]\(([^\)]+)\)')

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
        with open(md_file, encoding='utf-8') as f:
            content = f.read()

        for link_text, link_path in link_pattern.findall(content):
            if _should_skip_link(link_path):
                continue

            target_path, relative_to_docs = _resolve_link_path(link_path, md_file)

            if target_path.exists():
                continue

            # Check if it's an expected missing page
            if relative_to_docs and str(relative_to_docs) in expected_missing:
                print(f'⚠ Expected missing page: {link_path}')
                continue

            # Check if it's a valid anchor link
            if _is_valid_anchor_link(link_path, md_file):
                continue

            broken_links.append(
                {
                    'file': md_file.relative_to(PERLA_DIR),
                    'link_text': link_text,
                    'link_path': link_path,
                    'resolved_path': target_path,
                }
            )

    if broken_links:
        error_msg = 'Broken internal links found:\n'
        for link in broken_links:
            error_msg += f'\n  In {link["file"]}:'
            error_msg += f'\n    Link text: {link["link_text"]}'
            error_msg += f'\n    Link path: {link["link_path"]}'
            error_msg += f'\n    Resolved to (missing): {link["resolved_path"]}\n'
        pytest.fail(error_msg)


def test_required_notebooks_present():
    """Verify critical notebooks are present."""
    required_notebooks = [
        'query-perovskite-database.ipynb',
        'performance-evolution.ipynb',
        'bandgap-evolution.ipynb',
        'architecture-evolution.ipynb',
        'diversity-analysis.ipynb',
        'crabnet-perovskite-bandgap-prediction.ipynb',
        'ml-distribution-shift-case-study.ipynb',
        'perovscribe-analysis.ipynb',
        'perovskite-paperbot-plot.ipynb',
    ]

    notebooks_dir = DOCS_DIR / 'notebooks'
    missing = []

    for notebook in required_notebooks:
        notebook_path = notebooks_dir / notebook
        if not notebook_path.exists():
            missing.append(notebook)
        else:
            print(f'✓ {notebook}')

    assert not missing, f'Required notebooks missing: {", ".join(missing)}'


if __name__ == '__main__':
    # Run tests with verbose output
    pytest.main([__file__, '-v'])
