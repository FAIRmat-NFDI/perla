# Architecture & Pipeline

PERLA's architecture is designed for scalable, automated extraction and validation of perovskite solar cell data from scientific literature.
The system operates as a continuous pipeline that monitors publications, extracts data, validates findings, and updates the living database.

## System Overview

The pipeline consists of several interconnected components that work together to maintain a continuously updated, high-quality data archive.

## Core Components

### 1. Literature Monitoring ([`perla-extract`](https://github.com/lamalab-org/perla-extract))

- Monitors major publishers
- Filters publications based on perovskite-related keywords
- Handles full-text access and PDF retrieval

### 2. Data Extraction Engine ([`perla-extract`](https://github.com/lamalab-org/perla-extract))

- Extracts text from PDFs from papers
- Uses LLMs for text analysis
- Maintains publication metadata and provenance
- Extracts device parameters, experimental conditions, and performance metrics
- Validates extracted parameters against known physical constraints

### 3. Database Architecture (NOMAD plugin)([`nomad-perovskite-solar-cells-database`](https://github.com/FAIRmat-NFDI/nomad-perovskite-solar-cells-database))

- Built on the NOMAD platform
- Follows NOMAD schema standards for perovskite solar cells
- Uses existing tooling to, for example, process ions
- Provides integration with broader materials science ecosystem


### 4. Web Portal and API Access Layer ([`PERLA in NOMAD`](https://nomad-lab.eu/prod/v1/gui/search/perovskite-solar-cells-database))

- RESTful API for data queries and retrieval
- Web-based search and visualization tools
- Interactive data exploration capabilities