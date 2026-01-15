# Case Studies

These Jupyter notebooks demonstrate real-world applications of PERLA data for research and analysis. Each notebook combines data access, processing, and visualization to showcase different aspects of the perovskite solar cell database.

## Available Case Studies

### 🔍 [Query PERLA Database](../notebooks/query-perovskite-database.ipynb)
**Introduction to data access and basic analysis**

Learn how to:
- Connect to the PERLA database through NOMAD API
- Perform basic queries and filtering
- Extract and process device parameters
- Create simple visualizations

*Ideal for: First-time users and beginners*

### 📈 [Performance Evolution Analysis](../notebooks/performance-evolution.ipynb)
**Tracking efficiency improvements over time**

Explore:
- Historical trends in device performance
- Efficiency evolution patterns
- Statistical analysis of performance metrics
- Temporal correlations in device parameters

*Ideal for: Researchers interested in field development trends*

### 🌈 [Bandgap Evolution Analysis](../notebooks/bandgap-evolution.ipynb)
**Understanding bandgap optimization trends**

Investigate:
- Bandgap distribution changes over time
- Composition-bandgap relationships
- Optimal bandgap ranges for different applications
- Materials selection strategies

*Ideal for: Materials scientists and device engineers*

### 🏗️ [Architecture Evolution Analysis](../notebooks/architecture-evolution.ipynb)
**Device structure and design trends**

Analyze:
- n-i-p vs p-i-n architecture adoption
- Layer structure optimization
- Interface engineering trends
- Architecture-performance correlations

*Ideal for: Device physicists and engineers*

### 🎯 [Diversity Analysis](../notebooks/diversity_analysis.ipynb)
**Compositional and structural diversity trends**

Study:
- Chemical composition diversity over time
- Structural innovation patterns
- Novel material adoption rates
- Research direction indicators

*Ideal for: Research strategists and material discoverers*

### 🧠 [ML Prediction with CrabNet](../notebooks/crabnet-perovskite-bandgap-prediction.ipynb)
**Machine learning for property prediction**

Learn:
- Training ML models on PERLA data
- Bandgap prediction from composition
- Model validation and performance metrics
- Integration of experimental and computational data

*Ideal for: Computational researchers and ML practitioners*

## How to Use These Notebooks

### Option 1: Local Jupyter Environment
1. Clone the repository or download the notebooks
2. Install required dependencies (see each notebook for specific requirements)
3. Launch Jupyter: `jupyter lab` or `jupyter notebook`
4. Open and run the notebooks interactively

### Option 2: Cloud Platforms
- **Google Colab**: Upload notebooks and run in your browser
- **Binder**: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/FAIRmat-NFDI/perla/main?labpath=docs%2Fnotebooks)
- **JupyterHub**: Use your institution's JupyterHub instance

### Option 3: View Static Versions
If you just want to browse the analysis without running code:
- GitHub automatically renders notebooks with basic formatting
- NBViewer provides enhanced static viewing: [View on NBViewer](https://nbviewer.org/github/FAIRmat-NFDI/perla/tree/main/docs/notebooks/)

## Prerequisites

### Required Python Packages
```bash
pip install pandas numpy matplotlib seaborn plotly requests jupyter
```

### For ML Notebooks
```bash
pip install scikit-learn torch crabnet pymatgen
```

### Data Access
- No authentication required for public PERLA data
- Internet connection needed for API access
- Some notebooks include cached data for offline use

## Contributing

### Improve Existing Notebooks
- Report issues or bugs in the analysis
- Suggest improvements to visualizations
- Add explanatory text or comments

### Create New Case Studies
We welcome new notebooks that showcase:
- Novel analysis approaches
- Integration with other datasets
- Advanced visualization techniques
- Domain-specific applications

See our [Contributing Guide](../how_to/contribute_to_perla.md) for details.

## Feedback and Support

- **Issues**: Report problems on [GitHub Issues](https://github.com/FAIRmat-NFDI/perla/issues)
- **Discussions**: Join conversations about analysis approaches
- **Documentation**: Help improve notebook documentation

## Citation

When using these case studies in your research, please cite:
- The main PERLA publication (see [Citation Guidelines](../explanation/citation.md))
- Individual datasets and tools as referenced in each notebook
- The specific notebooks if they significantly contributed to your analysis

---

*These case studies demonstrate the power of PERLA's living database for enabling data-driven discovery in perovskite photovoltaics research.*