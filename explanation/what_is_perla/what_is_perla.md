# What is PERLA?

**PERLA** (PERovskite Living Archive) is an ecosystem for perovskite solar cell data built on the NOMAD platform. It addresses the fundamental challenge of keeping pace with rapidly growing publication rates in the field of perovskite photovoltaics.

## The Challenge

Perovskite solar cells are one of the fastest-growing research areas in photovoltaics, with thousands of publications produced annually. Traditional approaches to scientific data management rely on manual extraction and static databases, which cannot match the pace of new research output. This creates a bottleneck where valuable experimental insights remain locked in publications, unable to contribute to data-driven discovery.

## PERLA's Solution

PERLA transforms static publications into dynamic knowledge resources through automated data extraction and continuous database updates. The system combines:

- **Large Language Models (LLMs)** for intelligent text and figure analysis
- **Physics-based validation** for quality control and consistency checking
- **NOMAD integration** for FAIR data principles and interoperability
- **Continuous monitoring** of scientific literature sources

## Key Capabilities

### Automated Data Extraction
- Monitors RSS feeds from major publishers (Nature, Science, ACS, RSC, etc.)
- Extracts device parameters from text, tables, and figures
- Processes both experimental data and computational results
- Achieves >90% precision in data extraction tasks

### Physics-based Validation
- Cross-validates extracted parameters against physical constraints
- Identifies and flags inconsistent or anomalous data points

### Living Database Architecture
- Continuously updated with new publications
- Structured data following NOMAD schema definitions
- API access for programmatic data retrieval