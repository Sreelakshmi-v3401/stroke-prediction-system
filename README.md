# stroke-prediction-system

# 🧠 Stroke Prediction & Risk Analysis System

An end-to-end Machine Learning web application designed to predict the likelihood of a stroke in patients based on clinical parameters, lifestyle factors, and demographic details. Built with Python, Scikit-learn, and deployed interactively using Streamlit.

---

## 🚀 Key Features

- **Exploratory Data Analysis (EDA):** Comprehensive visualization of health metrics, correlations, and distribution patterns.
- **Outlier Capping (IQR Method):** Handled extreme values in features like `avg_glucose_level` and `bmi` without losing critical medical data.
- **Feature Scaling:** Applied `MinMaxScaler` to normalize data ranges for distance-based algorithms.
- **Class Imbalance Handling (SMOTE):** Generated synthetic data points for the minority class to prevent model bias.
- **Model Training & Comparison:** Evaluated multiple algorithms including KNN, SVM, Decision Trees, and Random Forest.
- **Interactive Web App:** Deployed a user-friendly prediction interface using **Streamlit**.

---

## 📊 Model Performance

- **Algorithm Used:** Random Forest Classifier
- **Accuracy:** ~93.73%
- **Evaluation Metrics:** Confusion Matrix, Precision, Recall, and F1-Score.

---

## 🛠️ Tech Stack

- **Language:** Python 
- **Libraries:** Pandas, NumPy, Scikit-learn, Imbalanced-learn (SMOTE), Matplotlib, Seaborn
- **Deployment:** Streamlit
- **Tools:** Git, Visual Studio Code, Jupyter Notebook

---

## ⚙️ Project Workflow

1. **Data Preprocessing:** Handling missing values (mean imputation) and encoding categorical features (`LabelEncoder`).
2. **Feature Engineering:** Outlier capping using IQR and numerical scaling using `MinMaxScaler`.
3. **Resampling:** Applying SMOTE on the training set to resolve class imbalance (Stroke vs. Non-Stroke).
4. **Model Building:** Training and hyperparameter tuning of Random Forest.
5. **Deployment:** Saving the trained model using `Pickle` and building the Streamlit UI (`app.py`).

---

## 🏃‍♂️ How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Sreelakshmi-v3401/stroke-prediction-system.git](https://github.com/Sreelakshmi-v3401/stroke-prediction-system.git)
   cd stroke-prediction-system
