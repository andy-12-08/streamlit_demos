import streamlit as st
import pandas as pd

# Memory package
from memory_profiler import profile


st.title("Streamlit Forms and Salary Calculator")

menu = ["Home", "About"]
choice  =  st.sidebar.selectbox("Menu", menu)

if choice == "Home":
    st.subheader("Forms Tutorial")

    # Salary Calculator
    ## Splitting a form into columns 
    with st.form(key='salaryform', clear_on_submit=True):
        col1,col2,col3 = st.columns([3,2,1])
        with col1:
            amount = st.number_input("Hourly Rate in $")
        with col2:
            hour_per_week = st.number_input("Hours Per Week", 1,120)
        with col3:
            st.text("Salary")
            submit_salary = st.form_submit_button(label='calculate')
    if submit_salary:
        with st.expander('Results'):
            daily = [amount*8]
            weekly = [amount*hour_per_week]
            # put the results in a dataframe
            df = pd.DataFrame({'hourly':amount, 'daily':daily, 'weekly':weekly})
            # transpose the dataframe
            st.dataframe(df.T)

    # Method 1: Context Manager Approach (with)
    with st.form(key='form1',clear_on_submit=True):
        firstname = st.text_input("First name")
        lastname = st.text_input("Last name")
        dob = st.date_input("Date of birth")
        submit_button = st.form_submit_button(label="Sign up")
    # Result of clicking the submit button can be coded inside or outside the form
    if submit_button:
        st.success(f"Hello {firstname} you have created an account")

    # Method 2: 
    form2 = st.form(key='form2',clear_on_submit=True)
    username = form2.text_input('username')
    jobtype = form2.selectbox('Job',['Dev','Data Scientist', 'Doctor'])
    submit_button2 = form2.form_submit_button("Login")

else:
    st.subheader("About")