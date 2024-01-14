import streamlit as st

def main():
    # Initialize the session state variable if it's not already set
    if 'my_variable' not in st.session_state:
        st.session_state['my_variable'] = 'From Main App Page'

    st.title("Streamlit Multi-Page")
    st.subheader('Main Page')
    # Access the variable from session state
    st.write(st.session_state['my_variable'])

if __name__ == '__main__':
    main()
