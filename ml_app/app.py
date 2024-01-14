import streamlit as st

from eda_app import run_eda_app
from ml_app import run_ml_app


def main():

    st.set_page_config(page_title='machine learning application',
                   page_icon="images/ml_image.png",
                   initial_sidebar_state="expanded" )

    menu = ['Home','EDA','ML','About']
    choice = st.sidebar.selectbox('Menu', menu)

    # Title Section
    html_head = """
<div>
    <marquee style="color: darkgoldenrod;font-size: 30px; padding-bottom:30px"> <b>Early detection can prevent adverse effect</b> </marquee>
    <div style="background-color:darkslategray;text-align: center; border-radius: 8px;">
        <h1> Early Stage DM Risk Data App</h1>
        <h5> Diabetes </h5>
    </div> 
</div>
"""
    st.markdown(html_head, unsafe_allow_html=True)

    if choice == 'Home':
        home_html = """
        <span>
            <h4 style="padding-top:30px;"> Home </h4>
        </span>
        """
        st.markdown(home_html,unsafe_allow_html=True)
        st.subheader('Early Stage Diabetes Risk Prediction App')
        st.write('This dataset contains the sign and symptoms data of newly diabetic or would be diabetic patient')
        st.markdown('#### Datasource ####')
        st.markdown('###### <span style="margin-left:20px;"> - https://archive.ics.uci.edu/ml/datasets/Early+stage+diabetes+risk+prediction+dataset. ######' , unsafe_allow_html=True)
        st.markdown('#### App Content ####')
        st.markdown('###### <span style="margin-left:20px;"> - EDA Section:</span> Exploratory Data Analysis of Data ######', unsafe_allow_html=True)
        st.markdown('###### <span style="margin-left:20px;"> - ML Section: ML Predictor App ######', unsafe_allow_html=True)

    elif choice == 'EDA':
        run_eda_app()
    
    elif choice == 'ML':
        run_ml_app()

    else:
        st.subheader('About')

if __name__ == '__main__':
    main()