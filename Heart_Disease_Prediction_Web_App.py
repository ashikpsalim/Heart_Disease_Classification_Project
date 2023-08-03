import numpy as np
import pickle
import streamlit as st

# loading the saved model
load_model = pickle.load(open("C:/Users/user/Complete ML & DS/Classification/trained_model.sav", 'rb'))

# function for prediction
def heart_disease_prediction(input_data):
    input_data_numpy_array_reshaped = np.asarray(input_data).reshape(1, -1)
    prediction = load_model.predict(input_data_numpy_array_reshaped)
    if prediction[0] == 1:
        return 'The patient has Heart Disease!'
    else:
        return 'No Heart Disease!'

def main():
    # title
    st.title("Heart Disease Prediction Web App")

    # input data from user
    age = st.number_input('Age', min_value=0, max_value=150, value=0)
    sex = st.selectbox('Sex', ['Male', 'Female'], index=0)
    
    # Mapping for Chest Pain (cp)
    cp_mapping = {
        'Typical Angina': 0,
        'Atypical Angina': 1,
        'Non-Anginal Pain': 2,
        'Asymptotic': 3
    }
    cp = st.selectbox('Chest Pain', list(cp_mapping.keys()), index=0)

    trestbps = st.number_input('Resting Blood Pressure', min_value=0, max_value=300, value=0)
    chol = st.number_input('Serum Cholesterol', min_value=0, max_value=600, value=0)
    fbs = st.selectbox('Fasting Blood Sugar', ['No', 'Yes'], index=0)
    restecg = st.selectbox('Resting Electrocardiograph (ECG)', ['0', '1'], index=0)
    thalach = st.number_input('Maximum Heart Rate', min_value=0, max_value=300, value=0)
    exang = st.selectbox('Exercise Induced Angina', ['No', 'Yes'], index=0)
    oldpeak = st.number_input('ST depression induced by exercise relative to rest', min_value=0.0, max_value=10.0, value=0.0)

    # Mapping for Slope of the peak exercise ST segment (slope)
    slope_mapping = {
        'Upsloping': 0,
        'Flat': 1,
        'Downsloping': 2
    }
    slope = st.selectbox('Slope of the peak exercise ST segment', ['Upsloping', 'Flat', 'Downsloping'], index=0)

    ca = st.number_input('Number of major vessels (0–3) colored by fluoroscopy', min_value=0, max_value=3, value=0)

    # Mapping for Thalassemia (thal)
    thal_mapping = {
        'Normal': 1,
        'Fixed Defect': 3,
        'Reversible Defect': 2
    }
    thal = st.selectbox('Thalassemia', ['Normal', 'Fixed Defect', 'Reversible Defect'], index=0)

    # Code for prediction
    diagnosis = ''

    # Button for prediction
    if st.button('Result'):
        # Convert categorical variables to numeric values based on mappings
        sex = 1 if sex == 'Male' else 0
        cp = cp_mapping[cp]
        fbs = 1 if fbs == 'Yes' else 0
        restecg = int(restecg)
        exang = 1 if exang == 'Yes' else 0
        slope = slope_mapping[slope]
        thal = thal_mapping[thal]

        input_data = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        diagnosis = heart_disease_prediction(input_data)

    st.success(diagnosis)

if __name__ == '__main__':
    main()

