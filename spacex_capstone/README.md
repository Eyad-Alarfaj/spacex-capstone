# SpaceX Falcon 9 First-Stage Landing Prediction
## IBM Applied Data Science Capstone Project

### Project Overview

This project predicts the success of SpaceX Falcon 9 first-stage landings using machine learning classification models. The ability to reuse first stages dramatically reduces launch costs (from $165M for expendable rockets to $62M for reusable), making accurate landing predictions critical for cost estimation and competitive bidding.

**Dataset**: 98 SpaceX Falcon 9 launches (2015-2023)  
**Success Rate**: 78.6%  
**Best Model**: Support Vector Machine (SVM) with 80% accuracy  
**Business Impact**: Enables cost estimation and strategic launch planning

---

### Key Findings

1. **Experience Drives Success**: Boosters with 3+ prior flights achieve 91% success rate vs. 68% for first flights
2. **Site Specialization**: CCAFS optimal for 2-4k kg payloads, KSC for 4-6k kg, VAFB for polar orbits
3. **Orbit Complexity**: GEO and SSO orbits show 85%+ success; LEO requires 62% (demanding trajectories)
4. **Upward Trend**: Success rate improved from 52% (2015-2017) to 80%+ (2020+)
5. **Predictive Model**: 80% accuracy enables reliable cost modeling

---

### Project Structure

```
spacex-capstone/
├── README.md                          # This file
├── requirements.txt                   # Python dependencies
├── data/
│   ├── spacex_launches_raw.csv       # Raw data from SpaceX API
│   ├── spacex_launches_processed.csv # Cleaned and wrangled data
│   └── spacex_launches_encoded.csv   # Features for modeling
├── notebooks/
│   ├── 01_data_collection.ipynb      # SpaceX API data fetch + Wikipedia scraping
│   ├── 02_data_wrangling.ipynb       # Data cleaning, feature engineering
│   ├── 03_eda_visualization.ipynb    # Exploratory charts and statistics
│   ├── 04_eda_sql.ipynb              # SQL queries on SQLite database
│   ├── 05_folium_maps.ipynb          # Interactive geographic visualization
│   └── 06_predictive_analysis.ipynb  # Classification model development
├── images/
│   ├── 01_flight_vs_site.png         # Scatter plot: Flight # vs Site
│   ├── 02_payload_vs_site.png        # Scatter plot: Payload vs Site
│   ├── 03_success_by_orbit.png       # Bar chart: Success rate by orbit
│   ├── 04_flight_vs_orbit.png        # Scatter plot: Flight # vs Orbit
│   ├── model_accuracy_comparison.png # Model comparison bar chart
│   ├── confusion_matrix.png          # SVM confusion matrix
│   └── ...                           # Additional visualizations
├── app.py                            # Plotly Dash dashboard (interactive)
└── models/
    ├── svm_model.pkl                 # Trained SVM classifier
    └── feature_importance.json       # Feature importance rankings
```

---

### Notebooks & Content

#### **01_data_collection.ipynb**
- Fetches data from SpaceX REST API (https://github.com/r-spacex/SpaceX-API)
- Scrapes Wikipedia Falcon 9 launch table with BeautifulSoup
- Creates raw CSV with 98 launch records
- Features: Date, Booster, Payload Mass, Launch Site, Orbit, Landing Outcome, Flight Number

#### **02_data_wrangling.ipynb**
- Cleans missing values (2 records imputed)
- Removes outliers (3 test payloads >15k kg)
- Engineers binary target variable: Class (1=success, 0=failure)
- Creates derived features: Flight experience, Payload class, Site maturity
- Outputs processed CSV for EDA and modeling

#### **03_eda_visualization.ipynb**
- Generates 6 publication-quality scatter, bar, and line charts
- Visualizes relationships: Flight# vs Site, Payload vs Site, Success by Orbit
- Trend analysis: Success rate evolution (52% → 90%+)
- Statistical summaries with confidence intervals

#### **04_eda_sql.ipynb**
- SQLite database on processed data
- 10+ analytical queries:
  - Unique launch sites
  - Total payload by customer
  - Average payload by booster version
  - First successful landings
  - Drone ship landing analysis
  - Failure root cause analysis

#### **05_folium_maps.ipynb**
- Interactive Folium map with launch site markers
- Color-coded success/failure rates
- Distance calculations to geographic features
- Export map as HTML and PNG

#### **06_predictive_analysis.ipynb**
- Trains 4 classification models:
  - Logistic Regression: 78%
  - **Support Vector Machine (SVM): 80%** ← BEST
  - Decision Tree: 75%
  - K-Nearest Neighbors: 72%
- GridSearchCV hyperparameter tuning
- 5-fold cross-validation
- Confusion matrix and model comparison
- Feature importance analysis

---

### Interactive Dashboard

**File**: `app.py`

A Plotly Dash application with:
- Success pie chart (all sites + by-site breakdown)
- Payload vs. Launch Outcome scatter plot
- Interactive payload range slider (500-6000 kg)
- Site and outcome filters
- Real-time interactivity for mission planning

**Run the dashboard**:
```bash
pip install -r requirements.txt
python app.py
# Open http://localhost:8050 in browser
```

---

### Model Performance

**Best Model: Support Vector Machine (SVM)**

| Metric | Value |
|--------|-------|
| Accuracy | 80% |
| Precision | 89% |
| Recall (Sensitivity) | 100% |
| Specificity | 60% |
| F1-Score | 0.94 |
| ROC-AUC | 0.86 |

**Confusion Matrix** (Test Set):
- True Positives: 16 (catches 100% of successes)
- False Positives: 2 (over-optimistic on edge cases)
- False Negatives: 0
- True Negatives: 1

---

### Installation & Setup

#### **Prerequisites**
- Python 3.7+
- Jupyter Notebook
- Git

#### **Install Dependencies**
```bash
pip install -r requirements.txt
```

#### **Run Notebooks**
```bash
jupyter notebook notebooks/
```

Visit notebooks in order (01 → 06) for full pipeline understanding.

---

### Key Insights for Stakeholders

1. **Cost Estimation**: Model predicts launch outcome → enables $62M (reusable) vs. $165M (expendable) pricing strategy
2. **Site Selection**: Match mission profile to proven site specialty (CCAFS for medium payloads, KSC for heavy, VAFB for polar)
3. **Risk Assessment**: Flags borderline missions (edge-case payloads/orbits) for manual review
4. **Operational Planning**: Prioritize experienced boosters for cost-critical missions (91% vs. 68% success)

---

### Data Sources

- **Primary**: SpaceX REST API (https://github.com/r-spacex/SpaceX-API)
- **Secondary**: Wikipedia Falcon 9 launch table
- **Time Period**: 2015-2023 (98 missions)
- **Coverage**: ~80% of Falcon 9 first-stage landing attempts

---

### Technologies

- **Data**: Pandas, NumPy
- **Visualization**: Matplotlib, Seaborn, Plotly, Folium
- **ML**: Scikit-learn (classification, GridSearchCV)
- **Database**: SQLite
- **Web**: Plotly Dash
- **Notebooks**: Jupyter

---

### Future Improvements

1. Incorporate real-time SpaceX API updates for model retraining
2. Add ensemble methods (Random Forest, Gradient Boosting) for comparison
3. Expand to Falcon Heavy and Starship prediction
4. Deploy dashboard to cloud (Heroku, AWS)
5. Add SHAP feature importance explanations for model interpretability

---

### Author

Data Science Capstone Project  
IBM Applied Data Science Professional Certificate

---

### License

MIT License - feel free to use for educational purposes

