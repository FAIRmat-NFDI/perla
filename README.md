# PERLA - The PERovskite photovoltaics Living Archive

PERLA (The PERovskite photovoltaics Living Archive) is a comprehensive platform for analyzing and exploring perovskite solar cell research data. This repository contains the documentation hub that provides tutorials, guides, and interactive notebooks for working with perovskite datasets.

## Features

- **Interactive Notebooks**: Jupyter notebooks demonstrating data analysis techniques
- **Documentation**: Comprehensive guides following the Diátaxis framework
- **Data Analysis Tools**: Examples for querying and analyzing perovskite solar cell databases
- **Machine Learning Examples**: Tutorials on applying ML to perovskite research

## Quick Start

### Documentation

Visit the documentation at https://fairmat-nfdi.github.io/perla to explore:

- **Tutorials**: Step-by-step learning guides
- **How-to Guides**: Task-oriented instructions
- **Case Studies**: Real-world analysis examples
- **Reference**: Technical documentation

### Local Development

To build and serve the documentation locally:

```bash
# Clone this repository
git clone https://github.com/FAIRmat-NFDI/perla.git
cd perla

# Install dependencies
uv sync

# Prepare documentation (requires nomad-perovskite-solar-cells-database)
./scripts/prepare_docs.sh

# Serve locally
mkdocs serve
```

## Contributing

We welcome contributions! Please see our [contribution guide](docs/how_to/contribute_to_the_documentation.md) for detailed instructions on:

- Adding new notebooks
- Building documentation locally
- Testing changes
- Repository structure requirements

## Repository Structure

```
perla/
├── docs/                   # Documentation source files
│   ├── how_to/            # How-to guides
│   ├── tutorials/         # Learning-oriented tutorials
│   └── notebooks/         # Generated notebook files (not in git)
├── scripts/               # Build and utility scripts
├── tests/                 # Documentation tests
└── mkdocs.yml            # MkDocs configuration
```
