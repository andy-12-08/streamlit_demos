import streamlit as st

st.subheader('Home Page')
st.session_state['my_variable']
st.session_state['my_var_from_eda']

choice = st.sidebar.selectbox('submenu',['Pandas','Tensor Flow'])

if choice == 'Pandas':
    st.subheader('Pandas')


# def home_page():
#     # Ensure that this page is only accessible if 'my_variable' is already set in the session state
#     if 'my_variable' in st.session_state:
#         st.subheader('Home Page')
#         st.write(st.session_state['my_variable'])
#     else:
#         st.error("Variable not initialized in the session state.")

# if __name__ == '__main__':
#     home_page()
