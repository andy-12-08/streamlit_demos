import streamlit as st

# Load EDA Pkgs
import pandas as pd
import numpy as np

# Load Data Viz Pkgs 
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg') # TkAgg
import seaborn as sns
import plotly.express as px
import altair as alt


def main():
    st.title('Plotting with st.pyplot')
    df = pd.read_csv('iris.csv')
    st.dataframe(df.head())

    # Method 1
    fig, ax = plt.subplots()
    ax.scatter(*np.random.random(size=(2,100)))
    st.pyplot(fig)

    # Method 2
    fig = plt.figure()
    df['species'].value_counts().plot(kind='bar')
    st.pyplot(fig)

    # Method 3
    fig, ax = plt.subplots()
    df['species'].value_counts().plot(kind='bar')
    st.pyplot(fig)

    # Alternative for matplotlib
    fig = plt.figure()
    sns.countplot(df['species'])
    st.pyplot(fig)

    # Bar Chart
    # Using st.bar_chart
    st.bar_chart(df['sepal_length'])

    # Line Chart
    df2 = pd.read_csv('lang_data.csv')
    st.dataframe(df2.head())
    lang_list = df2.columns.tolist()
    lang_choices = st.multiselect('Choose Language', lang_list, default='Python')
    st.line_chart(df2[lang_choices])

    #st.area_chart(df2[lang_choices])



    # Using matplotlib for a line plot
    fig, ax = plt.subplots()
    ax.plot(df2['Week'], df2['Python'], marker=None)  # 'marker=o' makes it a scatter plot
    ax.set_xlabel('Week')  # Set the label for the x-axis
    ax.set_ylabel('Python')  # Set the label for the y-axis
    ax.set_title('Python Plot')  # Set the title for the plot
    st.pyplot(fig)

    # Using Plotly 
    # For a line plot
    fig = px.line(df2, x='C', y='Python', title='C vs Python')
    # For a scatter plot, uncomment the following line and comment the line plot line
    # fig = px.scatter(df2, x='C', y='Python', title='C vs Python')
    st.plotly_chart(fig)

    df3 = pd.read_csv('prog_languages_data.csv')
    st.dataframe(df3)
    fig = px.pie(df3, values='Sum', names='lang', title='Pie Chart of Languages')
    st.plotly_chart(fig)

    fig2 = px.bar(df3, x='lang',y='Sum')
    st.plotly_chart(fig2)

if __name__ == '__main__':
    main()
