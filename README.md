# 🧠 Mental Health Disorder Prediction System

An end-to-end Machine Learning project that predicts the presence of a mental health disorder based on demographic and psychological factors. The project includes data preprocessing, feature engineering, model comparison, hyperparameter tuning, and deployment using Streamlit.

---

## 📌 Project Overview

Mental health disorders have become increasingly prevalent worldwide. This project aims to assist in early detection by leveraging machine learning techniques to classify whether a person is likely to have a diagnosed mental health disorder based on various features.

---

## 🚀 Features

- Data preprocessing and feature encoding
- scaling
- Multiple machine learning models evaluation
- Hyperparameter tuning using GridSearchCV
- Model performance comparison
- Interactive Streamlit web application for real-time prediction

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Streamlit
- Matplotlib
- Seaborn

---

## 📊 Models Evaluated

| Model | Test Accuracy (%) |
|---------|----------------|
| K-Nearest Neighbors | 94.09 |
| Logistic Regression | **98.14** |
| Gradient Boosting | 96.41 |
| Random Forest | 97.04 |
| AdaBoost | 94.01 |
| Gradient Boosting Classifier | 96.41 |
| Decision Tree | 96.33 |
| XGBoost | 97.75 |
| Support Vector Machine | 98.02 |

### ⭐ Best Performing Model
**Logistic Regression**

- Test Accuracy: **98.14%**
- Train Accuracy: **98.07%**

---

## 📂 Project Structure

```text
Mental-Health-Prediction-System/
│
├── app.py
├── model_training.ipynb
├── mental_health_model.pkl
├── scaler.pkl
├── label_encoders.pkl
├── dataset.csv
├── requirements.txt
├── README.md
└── images/
```

---

## 🔄 Workflow

1. Data Collection
2. Data Cleaning
3. Feature Encoding
4. Feature Scaling
5. Train-Test Split
6. Model Training
7. Model Evaluation
8. Hyperparameter Tuning
9. Streamlit Deployment

---

## 📈 Performance Comparison

| Model | Train Accuracy (%) | Test Accuracy (%) |
|---------|-----------------|----------------|
| KNN | 97.27 | 94.09 |
| Logistic Regression | 98.07 | **98.14** |
| Gradient Boosting | 96.54 | 96.41 |
| Random Forest | 99.66 | 97.04 |
| AdaBoost | 93.94 | 94.01 |
| Gradient Boosting Classifier | 96.54 | 96.41 |
| Decision Tree | 100.00 | 96.33 |
| XGBoost | 99.52 | 97.75 |
| Support Vector Machine | 98.21 | 98.02 |

---

## 💻 Running the Application

### Clone the Repository

```bash
git clone https://github.com/yourusername/Mental-Health-Prediction-System.git
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Streamlit App

```bash
streamlit run app.py
```

---

## 🎯 Results

Among all the machine learning algorithms evaluated, **Logistic Regression achieved the highest test accuracy of 98.14%**, demonstrating excellent generalization performance and making it the final model selected for deployment.

---

## 📸 Application Screenshot

(Add screenshots of your Streamlit app here)

---

## 👨‍💻 Author

**Fathima Rifa**

- Python
- Machine Learning
- Data Science
- Streamlit
- Scikit-learn

---

### ⭐ If you found this project useful, don't forget to star the repository!
