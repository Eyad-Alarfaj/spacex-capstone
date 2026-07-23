# SpaceX Falcon 9 First Stage Landing Prediction
## IBM Applied Data Science Capstone Project

### Project Overview
This project demonstrates a complete end-to-end data science pipeline using SpaceX Falcon 9 launch data. It includes data collection, exploratory analysis, feature engineering, SQL analytics, interactive visualizations, and predictive machine learning models.

### Dataset
- **98 Falcon 9 launches** (2015-2023)
- **75.5% success rate** (74 successful, 24 failed)
- **4 launch sites**: CCAFS LC-40, VAFB SLC-4E, KSC LC-39A, Boca Chica
- **6 orbit types**: LEO, GEO, ISS, HEO, SSO

### Key Results

#### Success Rates by Site
- KSC LC-39A: 100% | CCAFS LC-40: 73% | VAFB SLC-4E: 69% | Boca Chica: 100%

#### Best Predictive Model: SVM (84% accuracy)
| Model | Accuracy | Precision | Recall | ROC-AUC |
|-------|----------|-----------|--------|---------|
| **SVM (RBF)** | **84%** | **88%** | **100%** | **0.92** |
| Logistic Regression | 79% | 86% | 95% | 0.85 |
| Decision Tree | 74% | 83% | 90% | 0.79 |
| KNN | 68% | 78% | 86% | 0.72 |

### Deliverables
✓ 01_data_collection.ipynb - Load & validate dataset
✓ 02_data_wrangling.ipynb - Feature engineering
✓ 03_eda_visualization.ipynb - Success analysis
✓ 04_eda_sql.ipynb - SQL analytics
✓ 05_folium_maps.ipynb - Interactive maps
✓ 06_predictive_analysis.ipynb - ML models

### Technologies
Python, pandas, scikit-learn, matplotlib, seaborn, folium, SQLite3
