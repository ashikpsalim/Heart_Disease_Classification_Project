# Heart_Disease_Classification_Project
This GitHub repository contains code and documentation for an end-to-end heart disease prediction project. The goal of this project is to predict the probability of heart disease in patients using machine learning techniques. The dataset used for this project is sourced from Kaggle and can be found at Heart Disease Classification.

**Project Overview**
---------------

**Dataset**: Heart Disease Classification Dataset from Kaggle.
**Objective**: Predict the probability of heart disease in patients.
**Approach**: The project involves data preprocessing, exploratory data analysis, model selection, hyperparameter tuning, evaluation, and deployment.
**Models Explored**: Three models were tried out:
1. Logistic Regression
2. K-Nearest Neighbors Classification
3. RandomForest Classification
**Selected Model**: Logistic Regression was chosen as the final model due to its performance and interpretability.
Key Steps
---------

**Data Preprocessing**: The dataset was cleaned and preprocessed to handle missing values and prepare features for modeling.
**Exploratory Data Analysis (EDA)**: An exploratory analysis of the dataset was performed to gain insights into the distribution and relationships of features.
**Modeling**: Three different models were implemented and evaluated for prediction. Logistic Regression showed promising results.
**Hyperparameter Tuning**: GridSearchCV was used to tune hyperparameters for the Logistic Regression model.
**Evaluation Techniques**: Various evaluation techniques including ROC and AUC curves, confusion matrix, and cross-validation were employed to assess model performance.
**Feature Importance**: Feature importance analysis revealed that features 'cp', 'restecg', and 'slope' had the highest impact on the model.
**Model Persistence**: The final Logistic Regression model was saved using pickle for future use.
**Deployment**: The trained model was deployed as a local web application using Streamlit.
Results
-------

The Logistic Regression model achieved an accuracy of approximately 88.52%. Various evaluation metrics demonstrated the effectiveness of the model in predicting heart disease probabilities.
Files
-------
heart-disease: containing the dataset.
End-to-End-heart-disease-classification: Jupyter notebooks detailing data preprocessing, EDA, and model building.
trained_model.sav: Saved Logistic Regression model using pickle.
Heart_Disease_Prediction Web_App: Files for deploying the model as a Streamlit web application.
