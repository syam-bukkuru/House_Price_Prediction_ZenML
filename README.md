
# 🏠 House Price Prediction

This project predicts house prices using a machine learning pipeline built with **ZenML**, **Scikit-learn**, and **MLflow**. It follows a clean MLOps workflow including data ingestion, preprocessing, outlier removal, model training, evaluation, and experiment tracking.

---

## 🛠️ Stack Overview

| Component Type       | Component Name             |
|----------------------|----------------------------|
| **Orchestrator**     | `default`                  |
| **Experiment Tracker** | `mlflow_tracker_prices_new` |
| **Model Deployer**   | `mlflow_prices_new`        |
| **Artifact Store**   | `default`                  |

ZenML Stack Label: `zenml:full_stack=True`

---

## 🧪 Model Pipeline

The training pipeline includes the following steps:

1. **Data Ingestion**
2. **Missing Value Handling**
3. **Feature Engineering (Log Transform)**
4. **Outlier Detection (Z-Score Method)**
5. **Train-Test Split**
6. **Model Building**:
   - `LinearRegression` wrapped in Scikit-learn pipeline
   - Numerical features: `SimpleImputer(mean)`
   - Categorical features: `SimpleImputer(mode)` + `OneHotEncoder`
   - MLflow Autologging enabled
7. **Model Evaluation**

---

## 📊 Model Performance

| Metric         | Value                         |
|----------------|-------------------------------|
| **Mean Squared Error (MSE)** | `0.0109`       |
| **R² Score**    | `0.9221`                      |

> 📈 The model explains **92% of variance** in house prices, indicating strong predictive power.

---

## 🔗 MLflow & ZenML Dashboards

- **ZenML Dashboard**: [http://127.0.0.1:8237](http://127.0.0.1:8237)
- **MLflow UI** (run locally):  
```bash
mlflow ui \
  --backend-store-uri 'sqlite:///mlflow.db' \
  --default-artifact-root ./mlruns \
  --host 127.0.0.1 \
  --port 5000
```

> Note: Make sure `mlruns` and `mlflow.db` exist in the root directory.

---

## 🖼️ Project Progress Snapshots

### 🔹 Day 5 - Pipeline Setup  
![Day 5](project%20progress/Day5.png)

### 🔹 Day 8 - MLflow Integration  
![Day 8](project%20progress/Day8.png)

### 🔹 Final Output Screenshot  
![Final Output](project%20progress/Day8.1.png)

---

## 📁 Project Structure

```
house_price_prediction/
│
├── analysis/
│   └── EDA_on_AmesHousing_dataset.ipynb
├── dataset/
├── extracted_data/
├── mlruns/
├── pipelines/
│   └── training_pipeline.py
├── src/
│   ├── ingest_data.py
│   ├── feature_engineering.py
│   ├── handle_missing_values.py
│   ├── outlier_detection.py
│   └── model_building.py
├── steps/
│   └── *_step.py (ZenML step implementations)
├── project progress/
│   └── Day5.png, Day8.png, Day8.png (Screenshots)
├── mlflow.db
├── venv/
└── README.md
```

---

## 🚀 How to Run

1. **Install Requirements**
   ```bash
   pip install -r requirements.txt
   ```

2. **Start MLflow Server**
   ```bash
   mlflow ui \
     --backend-store-uri sqlite:///mlflow.db \
     --default-artifact-root ./mlruns \
     --host 127.0.0.1 \
     --port 5000
   ```

3. **Run the Pipeline**
   ```bash
   python run_pipeline.py
   ```

---

## 📦 Dependencies

- `ZenML`
- `MLflow`
- `scikit-learn`
- `pandas`
- `seaborn`
- `matplotlib`

---

