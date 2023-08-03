# Heart_Disease_Classification_Project
This GitHub repository contains code and documentation for an end-to-end heart disease prediction project. The goal of this project is to predict the probability of heart disease in patients using machine learning techniques. The dataset used for this project is sourced from Kaggle and can be found at Heart Disease Classification.Check out deployed web app on: https://heartdiseasepredictionwebapp.streamlit.app/

Project Overview
---------------

1. **Dataset**: Heart Disease Classification Dataset from Kaggle.
2. **Objective**: Predict the probability of heart disease in patients.
3. **Approach**: The project involves data preprocessing, exploratory data analysis, model selection, hyperparameter tuning, evaluation, and deployment.
4. **Models Explored**: Three models were tried out:
i. Logistic Regression
ii. K-Nearest Neighbors Classification
iii. RandomForest Classification
**Selected Model**: Logistic Regression was chosen as the final model due to its performance and interpretability.
Key Steps
---------

1. **Data Preprocessing**: The dataset was cleaned and preprocessed to handle missing values and prepare features for modeling.
2. **Exploratory Data Analysis (EDA**): An exploratory analysis of the dataset was performed to gain insights into the distribution and relationships of features.
3. **Modeling**: Three different models were implemented and evaluated for prediction. Logistic Regression showed promising results.
4. **Hyperparameter Tuning**: GridSearchCV was used to tune hyperparameters for the Logistic Regression model.
5. **Evaluation Techniques**: Various evaluation techniques including ROC and AUC curves, confusion matrix, and cross-validation were employed to assess model performance.
6.**Feature Importance**: Feature importance analysis revealed that features 'cp', 'restecg', and 'slope' had the highest impact on the model.
7. **Model Persistence**: The final Logistic Regression model was saved using pickle for future use.
8. **Deployment**: The trained model was deployed as a local web application using Streamlit.

Result
----------
The Logistic Regression model achieved an accuracy of approximately 88.52%. Various evaluation metrics demonstrated the effectiveness of the model in predicting heart disease probabilities.

Files
----------

1. heart-disease: containing the dataset.
2. End-to-End-heart-disease-classification: Jupyter notebooks detailing data preprocessing, EDA, and model building.
3. trained_model.sav: Saved Logistic Regression model using pickle.
4. Heart_Disease_Prediction Web_App: Files for deploying the model as a Streamlit web application.
