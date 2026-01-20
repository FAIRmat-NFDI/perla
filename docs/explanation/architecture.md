# Architecture & Pipeline

PERLA's architecture is designed for scalable, automated extraction and validation of perovskite solar cell data from scientific literature.
The system operates as a continuous pipeline that monitors publications, extracts data, validates findings, and updates the living database.

## System Overview

The pipeline consists of several interconnected components that work together to maintain a continuously updated, high-quality data archive.

## Core Components

### 1. Literature Monitoring ([`perla-extract`](https://github.com/lamalab-org/perla-extract))

- Monitors major publishers
- Filters publications based on perovskite-related keywords
- Handles full-text access and PDF processing
- Maintains publication metadata and provenance
- Extracts text from PDFs

### 2. Data Extraction Engine ([`perla-extract`](https://github.com/lamalab-org/perla-extract))

- Leverages LLMs for intelligent text analysis
- Extracts device parameters, experimental conditions, and performance metrics
- Processes both structured (tables) and unstructured (text) data sources

### 3. Physics-based Validation ([`perla-extract`](https://github.com/lamalab-org/perla-extract))

- Validates extracted parameters against known physical constraints
- Achieves >90% precision in data extraction tasks on most relevant parameters

### 4. Database Architecture ([`nomad-perovskite-solar-cells-database`](https://github.com/FAIRmat-NFDI/nomad-perovskite-solar-cells-database))

- Built on the NOMAD platform for materials science data
- Follows NOMAD schema standards for perovskite solar cells
- Uses existing tooling to, for example, process ions
- Inherits NOMAD's FAIR data principles and infrastructure
- Provides seamless integration with broader materials science ecosystem


### 5. API and Access Layer ([`nomad-perovskite-solar-cells-database`](https://github.com/FAIRmat-NFDI/nomad-perovskite-solar-cells-database))

- RESTful API for data queries and retrieval
- GraphQL interface for complex, nested queries
- Web-based search and visualization tools
- Interactive data exploration capabilities
- Export functionality for multiple formats