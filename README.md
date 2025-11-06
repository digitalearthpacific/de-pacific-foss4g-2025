# FOSS4G 2025 Workshop – Digital Earth Pacific

**Notebook Title**: *QField Integration into Machine Learning Landcover Classification*  
**Location Focus**: Auckland, New Zealand  
**Hosted by**: Digital Earth Pacific at AUT

## Overview

This Jupyter Notebook demonstrates a complete workflow for integrating QField-collected landcover data into a machine learning pipeline using cloud-native Earth observation datasets. It is designed for participants of the **FOSS4G 2025** workshop.

## Workflow Summary

The notebook is structured into **three main parts**:

1. **Data Preparation**
   - Define Area of Interest (AOI)
   - Load Sentinel-1, Sentinel-2, and elevation data
   - Compute NDVI and NDBI indices
   - Merge datasets and interpolate onto label points

2. **Model Training & Validation**
   - Train a Random Forest classifier
   - Evaluate using accuracy, F1-score, and Cohen’s Kappa
   - Analyze feature importance

3. **Prediction & Visualization**
   - Generate landcover maps
   - Compare RGB composites with predictions
   - Export results

## Requirements

Install dependencies using:

```bash
pip install -r requirements.txt

## Files

- `foss4g_workshop.ipynb` – Main notebook
- `lulc_auckland_v3.gpkg` – GeoPackage with labeled landcover points
- `requirements.txt` – Python dependencies
- `utils.py` – Custom functions for loading and preprocessing data

## Data Sources

- **Sentinel-2 L2A** – Optical imagery
- **Sentinel-1 GRD** – Radar backscatter
- **Copernicus DEM** – Elevation model
- **Land Cover Database v5.0** – Label data via LRIS Portal

## Objectives

- Learn to integrate field-collected data with EO datasets
- Apply machine learning for landcover classification
- Explore cloud-native geospatial workflows using STAC and Dask

## License

This project is released under **CC0 1.0 Universal** (Public Domain Dedication).

## Acknowledgements

This workshop is part of the Digital Earth Pacific initiative and wwill be presented at **FOSS4G 2025 Global Conference**. Special thanks to contributors and participants supporting open geospatial science in the Pacific.

## Questions or Feedback

For questions or feedback, feel free to reach out to the authors:

- Philippine Laroche at philippinel@spc.int  
- Kamsin Raju at kamsinr@spc.int
