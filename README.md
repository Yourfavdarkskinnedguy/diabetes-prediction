
## **🩺 Diabetes Prediction Using Machine Learning**

[link to web service](https://diabetes-prediction-3nj0.onrender.com/)


**📌 Project Overview**

This project is a **Flask-based web application** that predicts whether an individual is diabetic or non-diabetic based on several health-related features. The model is trained using **machine learning** techniques and deployed using a Flask API.

### **🚀 Features**

The model considers the following **health indicators** to make predictions:

* **Age** – Age of the individual
* **Pregnancies** – Number of times pregnant
* **BMI** – Body Mass Index
* **Glucose** – Blood sugar level
* **BloodPressure** – Blood pressure level
* **HbA1c** – Hemoglobin A1c percentage (used for diabetes diagnosis)
* **LDL** – Low-Density Lipoprotein (bad cholesterol)
* **HDL** – High-Density Lipoprotein (good cholesterol)
* **Triglycerides** – Type of fat (lipid) in the blood
* **WaistCircumference** – Measurement of the waist
* **HipCircumference** – Measurement of the hips
* **WHR** – Waist-to-Hip Ratio
* **FamilyHistory** – Whether the individual has a family history of diabetes
* **DietType** – Type of diet followed (e.g., vegetarian, non-vegetarian, keto)
* **Hypertension** – Whether the individual has high blood pressure
* **MedicationUse** – Whether the individual is on any medication related to diabetes

### **🛠 Tech Stack**

* **Programming Language** : Python
* **Framework** : Flask
* **Libraries** : NumPy, Pandas, Scikit-learn, Pickle
* **Frontend** : HTML, CSS
* **Deployment** : Flask API

### **📁 Dataset**

* The dataset consists of patient records with the features listed above.
* Preprocessing steps include handling missing values, feature scaling, and encoding categorical variables.
* The model is trained on labeled data where **1 = Diabetic** and  **0 = Non-Diabetic** .

### **🎯 Model Used**

* The machine learning model is trained using  **Random Forest Classifier** .
* The model is saved as a **Pickle file (`diabetes_model.pkl`)** and loaded in Flask for predictions.
