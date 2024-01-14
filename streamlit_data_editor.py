import streamlit as st
import pandas as pd
import time

# # import custom function
# from file_downloads import download_file


timestr = time.strftime("%Y%m%d-%H%M%S")

st.title("Streamlit Data Editor App")

menu = ['Home', 'About']
choice = st.sidebar.selectbox('Menu', menu)


if choice == 'Home':
    st.subheader('Editor')
    data_file = st.file_uploader('upload csv', type=['csv'])
    if data_file is not None:
        df = pd.read_csv(data_file)
        # editable/saveable form 
        with st.form(key='editor_form'):
            edited_df = st.data_editor(df)
            save_button = st.form_submit_button('save')
        if save_button:
            # one way
            # csv_downloader = download_file(edited_df,'csv')
            # csv_downloader.file_download()

            # another way
            final_df = edited_df.to_csv()
            new_filename = f'{data_file.name}_{timestr}.csv'
            st.download_button(label='Download data as csv',data=final_df,file_name=new_filename,mime='/text/csv')



else:
    st.subheader('About')
    