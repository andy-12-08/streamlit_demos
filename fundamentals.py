# import required packages 
import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np
import plotly.express as px

st.set_page_config(page_title="ML",
                   page_icon='HER.png',
                   initial_sidebar_state="collapsed")

st.sidebar.success("Menu")

#df = pd.read_csv('iris.csv')
    
#st.dataframe(df)
st.title("Plotting in streamlit with plotly")
df = pd.read_csv("prog_languages_data.csv")
st.dataframe(df)

fig = px.pie(df,values='Sum', names='lang', title='Pie Chart of Languages')
st.plotly_chart(fig)

fig2 = px.bar(df,x='lang', y='Sum', title='Bar Chart of Languages')
st.plotly_chart(fig2)


mycode = '''
def sayhello():
    print('Hello streamlit lovers')
'''

st.code(mycode)

name = "Andrew"
if st.button('submit'):
    st.write(f"Name: {name.upper()}")

status = st.radio("What is your status",("Active","Inactive"))

if status == "Active":
    st.success("You are active")
elif status == "Inactive":
    st.warning("Inactive")

if st.checkbox("show/hide"):
    st.text("showing something")

with st.expander("python"):
    st.success("yes")
    st.text("dropdown")
    st.radio("What do you prefer",("Fast","Slow"))

my_lang = ["python", "Go", "Julia", "Rust"]
choice = st.selectbox("Language",my_lang)
st.write(f"you selected {choice}")

spoken_lang = ("English", "French","Spanish", "German")
my_spoken_lang = st.multiselect("Spoken Language", spoken_lang)

age = st.slider("Age",1,100,[5,90])


img = Image.open("HER.png")
st.image(img)

message = st.text_area("Enter Message")

if st.button("submit", key='text_area'):
    st.text(message)

myappointments = st.date_input("Appointment")


