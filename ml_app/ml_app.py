import streamlit as st
import joblib
import os
import numpy as np
import pandas as pd
from eda_app import encode_data

attribute_info = """
- Age: 20-65		
- Sex: 1. Male, 0.Female		
- Polyuria: 1.Yes, 0.No.		
- Polydipsia: 1.Yes, 0.No.		
- sudden weight loss: 1.Yes, 0.No.		
- weakness: 1.Yes, 0.No.		
- Polyphagia: 1.Yes, 0.No.		
- Genital thrush: 1.Yes, 0.No.		
- visual blurring: 1.Yes, 0.No.		
- Itching: 1.Yes, 0.No.		
- Irritability: 1.Yes, 0.No.		
- delayed healing: 1.Yes, 0.No.		
- partial paresis: 1.Yes, 0.No.		
- muscle stiffness: 1.Yes, 0.No.		
- Alopecia: 1.Yes, 0.No.		
- Obesity: 1.Yes, 0.No.		
- Class: 1.Positive, 0.Negative.
"""


#Load ML Models
@st.cache_data
def load_model(model_file):
    loaded_model = joblib.load(open(os.path.join(model_file),'rb'))
    return loaded_model

def run_ml_app():

    st.subheader('ML Prediction')
    with st.expander('Attribute Information'):
        st.markdown(attribute_info)

    col1, col2 = st.columns(2)

    with col1:
        Age = st.number_input('Age',10,100)
        Gender = st.radio('Gender',('Male','Female'))
        Polyuria = st.radio("Polyuria",['No','Yes'])
        Polydipsia = st.radio("Polydipsia",['No','Yes'])
        sudden_weight_loss = st.selectbox("Sudden_weight_loss",['No','Yes'])
        weakness = st.radio("weakness",['No','Yes'])
        polyphagia = st.radio("Polyphagia",['No','Yes'])
        genital_thrush = st.selectbox("Genital_thrush",['No','Yes'])
    
    with col2:
        visual_blurring = st.selectbox('Visual_blurring',('No','Yes'))
        itching = st.radio("Itching",['No','Yes'])
        irritability = st.radio("Irritability",['No','Yes'])
        delayed_healing = st.radio("delayed_healing",['No','Yes'])
        partial_paresis = st.selectbox("Partial_paresis",['No','Yes'])
        muscle_stiffness = st.radio("muscle_stiffness",['No','Yes'])
        alopecia = st.radio("alopecia",['No','Yes'])
        obesity = st.select_slider("obesity",['No','Yes'])

    with st.expander("Your Selected Options"):
        results = {'Age':Age,
                   'Gender':Gender,
                   'Polyuria':Polyuria,
                   'Polydipsia':Polydipsia,
                   'sudden weight loss':sudden_weight_loss,
                   'weakness':weakness,
                   'Polyphagia':polyphagia,
                   'Genital thrush':genital_thrush,
                   'visual blurring':visual_blurring,
                   'itching':itching,
                   'Irritability':irritability,
                   'delayed healing':delayed_healing,
                   'partial paresis':partial_paresis,
                   'muscle stiffness':muscle_stiffness,
                   'Alopecia':alopecia,
                   'Obesity':obesity}
        
        results_df = pd.DataFrame([results])
        st.dataframe(results_df)
        results_df_encoded = encode_data(results_df)
        st.dataframe(results_df_encoded)

    with st.expander('Prediction'):
        # single sample with multiple features
        single_sample = np.array([results_df_encoded.iloc[0]])
        model = load_model('models/logistic_regression_model_diabetes_1_13_2024.pkl')
        prediction = model.predict(single_sample)
        pred_prob = model.predict_proba(single_sample)
        # st.write(prediction)
        # st.write(pred_prob)

        if prediction == 1:
            st.warning(f'Positive Risk: {prediction[0]}')
            pred_probability_score = {'Negative Risk': pred_prob[0][0]*100,
                                      'Positive Risk': pred_prob[0][1]*100}
            st.write(pred_probability_score)
        else:
            st.success(f'Negative Risk: {prediction[0]}')
            pred_probability_score = {'Negative Risk': pred_prob[0][0]*100,
                                      'Positive Risk': pred_prob[0][1]*100}
            st.write(pred_probability_score)

        
if __name__ == "__main__":
    run_ml_app()
 