import streamlit as st

def main():

    st.title('streamlit themes')
    storage = []
    with st.form(key='form1'):
        st.subheader('Home')
        name = st.text_input('name')
        st.multiselect('work',['Data Scientist','Doctor','Developer'])
        message = st.text_area('Message')
        submit = st.form_submit_button('submit') 
    if submit:
        st.write(f'Welcome {name}!')
        st.write(message)
        st.success('Submitted')
        storage.append({'name':name,'message':message})
        st.write(storage)

if __name__ == '__main__':
    main()
