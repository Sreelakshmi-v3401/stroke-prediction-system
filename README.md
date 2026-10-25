# 🧠 Stroke Prediction & Risk Analysis System

A Machine Learning web application designed to predict stroke risk in patients based on clinical and lifestyle parameters, built with Python and deployed using Streamlit.

---

## 🚀 Tech Stack
- **Language:** Python
- **Libraries:** Scikit-learn, Pandas, NumPy, SMOTE, Matplotlib, Seaborn
- **Framework:** Streamlit
- **Model:** Random Forest Classifier (93.73% Accuracy)

---

## ⚙️ Project Workflow
1. **Data Preprocessing:** Missing value imputation and Outlier Capping (`avg_glucose_level`, `bmi` using IQR).
2. **Feature Scaling:** Normalized values using `MinMaxScaler`.
3. **Resampling:** Handled class imbalance using **SMOTE**.
4. **Deployment:** Interactive web interface via Streamlit.

---

