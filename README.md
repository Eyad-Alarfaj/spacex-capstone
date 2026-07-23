# SpaceX Falcon 9 First Stage Landing Prediction
## IBM Applied Data Science Capstone

Predicting whether the Falcon 9 first stage lands successfully — the factor that determines whether a launch costs $62M or $165M+.

## Final Presentation
**[Final_Presentation_SpaceX_Capstone.pdf](Final_Presentation_SpaceX_Capstone.pdf)** — 24-slide deck with all methodology, charts, map, dashboard, and model results.

## Dataset
98 Falcon 9 launches (2015-09-28 → 2023-09-27) · 74 successful landings, 24 failures (75.5%)

## Notebooks (all executed, outputs included)
| Notebook | Purpose |
|---|---|
| `01_data_collection.ipynb` | Load & validate 98 launch records |
| `02_data_wrangling.ipynb` | Target creation, feature engineering, one-hot encoding |
| `03_eda_visualization.ipynb` | EDA charts: site, orbit, payload, experience, yearly trend |
| `04_eda_sql.ipynb` | Six SQL queries against SQLite |
| `05_folium_maps.ipynb` | Interactive launch-site map (`spacex_map.html`) |
| `06_predictive_analysis.ipynb` | Four classifiers, stratified 80/20 split |

## Key Results
- **Success by site:** Boca Chica 100% · KSC LC-39A 81% · VAFB SLC-4E 80% · CCAFS LC-40 68%
- **Success by orbit:** ISS 94% · GEO 94% · LEO 83% · SSO 44% · HEO 25%
- **Learning curve:** 50% (2015–16) → 69% (2017–19) → 89% (2020–23)
- **Booster experience:** 51% success for new boosters → 83% (1–2 landings) → 100% (3+)
- **Payload penalty:** failed flights average ~585 kg heavier than successes

## Model Performance (20-flight held-out test set)
| Model | Accuracy | Precision | Recall | F1 |
|---|---|---|---|---|
| **SVM (RBF)** ⭐ | **90%** | **88%** | **100%** | **0.94** |
| Logistic Regression | 85% | 88% | 93% | 0.90 |
| Decision Tree | 85% | 88% | 93% | 0.90 |
| KNN (k=5) | 85% | 88% | 93% | 0.90 |

Best model: **SVM (RBF)** — confusion matrix TP=15, TN=3, FP=2, FN=0. 100% recall means no successful landing is ever missed. Saved as `svm_model.pkl`.

## Dashboard & Map
- `spacex_dash_dashboard.html` — 4-panel Plotly Dash dashboard
- `spacex_map.html` — Folium interactive map
- `charts/` — all presentation figures

## Reproduce
```bash
pip install pandas numpy scikit-learn matplotlib seaborn folium plotly jupyter
jupyter nbconvert --execute --inplace 0*.ipynb
```

**Author:** Eyad Alarfaj
