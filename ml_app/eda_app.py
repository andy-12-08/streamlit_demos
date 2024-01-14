import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import seaborn as sns
import plotly.express as px

# ML libraries 
from sklearn.preprocessing import LabelEncoder

@st.cache_data
def load_data(data):
    df = pd.read_csv(data)
    return df

def encode_data(df):
    for col in df.columns:
        if col != 'Age':
            df[col] = df[col].map({'Yes': 1, 'No': 0,'Male':1,'Female':0,'Positive':1,'Negative':0})
    return df

def run_eda_app():

    st.subheader("From Exploratory Data Analysis")

    df = load_data('/data/diabetes_data_upload.csv')  # load it at the top because other sections might use it

    submenu = ['Descriptive','Plots']
    choice = st.sidebar.selectbox('Submenu',submenu)

    if choice == 'Descriptive':
        st.dataframe(df)

        col1,col2,col3 = st.columns(3)
        with col1:
            with st.expander("Data Types"):
                st.dataframe(df.dtypes)
        with col2:
            with st.expander("Descriptive Summary"):
                st.dataframe(df.describe())
        with col3:
            with st.expander("Class Distribution"):
                st.dataframe(df['class'].value_counts())


    else:
        st.subheader('Plots')
        col1,col2 = st.columns([2,1])

        with col1:
            with st.expander("Gender Distribution Plot"):

                ## method_1 (using plotly - piechart)
                gen_df = pd.DataFrame(list(dict(df['Gender'].value_counts()).items()),columns=['Gender','count'])
                fig1 = px.pie(gen_df, names='Gender', values='count', title='Pie Chart of Gender')
                st.plotly_chart(fig1, use_container_width=True)

                ## method_2 (using seaborn - bar chart)
                fig2 = plt.figure()
                #sns.countplot(df['Gender'])
                sns.countplot(x='Gender', data=df, palette='Set1')
                sns.set(style='darkgrid')
                st.pyplot(fig2)

            with st.expander("Class Distribution Plot"):
                ## method_1 (using plotly - piechart)
                gen_df = pd.DataFrame(list(dict(df['class'].value_counts()).items()),columns=['class','count'])
                fig1 = px.pie(gen_df, names='class', values='count', title='Pie Chart of Gender')
                st.plotly_chart(fig1, use_container_width=True)

                ## method_2 (using seaborn - bar chart)
                fig2 = plt.figure()
                #sns.countplot(df['Gender'])
                sns.countplot(x='class', data=df, palette='Set1')
                sns.set(style='darkgrid')
                st.pyplot(fig2)

        with col2:
            with st.expander("Gender Distribution Table"):
                st.dataframe(df['Gender'].value_counts())

            with st.expander("Class Distribution Table"):
                st.dataframe(df['class'].value_counts())

        with st.expander("Age Distribution Chart"):

            # Create the histogram using Plotly Express
            fig = px.histogram(df, x='Age', nbins=10, title='Age Distribution')

            fig.update_layout(
            #xaxis_showgrid=True,  # Show the x-axis gridlines
            #xaxis_gridcolor='lightgrey',  # You can change the color if needed
            #plot_bgcolor='white'  # Set the background color to white for better visibility
        )
            # Adjust the gap between bars
            fig.update_traces(marker_line_width=1, marker_line_color='black')  # Add lines between bars for clarity
            fig.update_layout(bargap=0.2)  # Adjust the gap between bars (0.2 is an example value)

            st.plotly_chart(fig, use_container_width=True)


        with st.expander("Outlier Visualization"):
            fig= px.box(df, x='Age', color='Gender')
            st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    run_eda_app()
