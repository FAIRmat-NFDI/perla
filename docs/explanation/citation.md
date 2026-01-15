# Citation Guidelines

When using PERLA data, tools, or insights in your research, please follow these citation guidelines to ensure proper attribution and support the continued development of the ecosystem.

## Citing PERLA

### Main Citation

When referencing PERLA in general, please cite our main publication:

```
[PLACEHOLDER - Main PERLA paper citation]
```

### Specific Components

For specific aspects of PERLA, consider additional citations:

**For the NOMAD platform integration:**
```
[PLACEHOLDER - NOMAD platform citation]
```

**For the extraction pipeline:**
```
[PLACEHOLDER - Perla-extract tool citation if applicable]
```

## Data Attribution

### Dataset Citation

When using PERLA database entries in your research:

```
PERLA Perovskite Solar Cell Database, accessed [DATE], 
DOI: [PLACEHOLDER_DOI], https://nomad-lab.eu/prod/v1/staging/gui/search/perovskite-solar-cells-database
```

### Individual Publications

PERLA maintains full provenance for all extracted data. When using specific extracted parameters, consider also citing the original source publications. This information is available in the metadata for each database entry.

## Usage Examples

### Research Paper
```latex
\documentclass{article}
\begin{document}

We analyzed perovskite solar cell performance trends using the PERLA database \cite{perla_main}, 
which provides continuously updated extraction of device parameters from the scientific literature.
The dataset contains over X entries extracted from Y publications through automated LLM-based 
analysis with physics-based validation.

\bibliography{references}
\end{document}
```

### Data Analysis Code
```python
# Example Python code citation
"""
Data source: PERLA Perovskite Solar Cell Database
Citation: [PLACEHOLDER - Main PERLA citation]
Accessed: 2024-XX-XX
URL: https://nomad-lab.eu/prod/v1/staging/gui/search/perovskite-solar-cells-database
"""

import requests
# Your analysis code here...
```

### Presentation/Poster
```
Data Source: PERLA - Perovskite Extraction & Research Living Archive
Citation: [PLACEHOLDER - Main PERLA citation]
Database: https://nomad-lab.eu/prod/v1/staging/gui/search/perovskite-solar-cells-database
```

## Acknowledgments

### Funding Sources
Please acknowledge the funding sources that support PERLA:

```
We acknowledge the FAIRmat-NFDI consortium and the NOMAD Centre of Excellence 
for supporting the development and maintenance of the PERLA ecosystem.
```

### Community Contributions
PERLA benefits from community feedback and contributions. Consider acknowledging:

```
We thank the PERLA community for data validation and continuous improvement 
of the extraction and validation processes.
```

## Guidelines for Different Use Cases

### Academic Publications
- Always cite the main PERLA publication
- Include dataset access date and version if applicable
- Consider citing original source papers for specific data points
- Acknowledge funding sources in acknowledgments section

### Conference Presentations
- Include PERLA logo and citation on slides using the data
- Provide brief description of PERLA's automated extraction approach
- Include URL for database access

### Reports and Documentation
- Provide full citation and DOI when available
- Include methodology description for data extraction
- Note any limitations or filtering applied to the dataset

### Software and Tools
- Include citation in code comments and documentation
- Provide proper attribution in user interfaces
- Link to PERLA documentation and resources

## Supporting PERLA

### How Citations Help
Proper citations help PERLA by:
- Demonstrating impact and utility to funding agencies
- Supporting continued development and maintenance
- Building community awareness and adoption
- Enabling tracking of research applications

### Other Ways to Support
- Provide feedback on data quality and extraction accuracy
- Contribute to documentation and tutorials  
- Report issues and suggest improvements
- Collaborate on tool development and integration

## Contact for Attribution Questions

If you have questions about proper attribution or citation:
- Check the [FAQ section](../reference/faq.md)
- Open an issue on [GitHub](https://github.com/FAIRmat-NFDI/perla)
- Contact the development team directly

## License Information

PERLA data and tools are provided under [PLACEHOLDER_LICENSE]. Please ensure your usage complies with the license terms and includes appropriate attribution as specified.

## Updates to Citation Guidelines

Citation guidelines may be updated as new publications and DOIs become available. Check this page regularly for the most current citation information.

---

*Thank you for properly citing PERLA and supporting open science practices in materials research!*