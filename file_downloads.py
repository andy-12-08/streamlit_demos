import streamlit as st
import pandas as pd
import streamlit.components as stc

import pyautogui
from PIL import Image

def take_screenshoot_and_save():
    # Take screenshot
    # x,y,width, height
    screenshot = pyautogui.screenshot(region=(100,100,800,600))
    filename = "streamlit_page.png"
    screenshot.save(filename)


### Fxn Approach
# Utils 
import base64
import time

timestr = time.strftime("%Y%m%d-%H%M%S")
# You can also try
# timestr = time.strftime("%Y-%m-%d-%H:%M:%S")

# def text_downloader(raw_text):
#     # Encode the text to bytes, then to Base64
#     b64 = base64.b64encode(raw_text.encode()).decode()
#     # Create the file name
#     new_filename = f"new_text_file_{timestr}.txt"
#     st.markdown("##### Download File #####") 
#     # Create the href string for downloading
#     href = f'<a href="data:file/txt;base64,{b64}" download="{new_filename}">Click Here!!</a>'
#     # Display the download link
#     st.markdown(href,unsafe_allow_html=True)



# def text_downloader(raw_text):
#     b64 = base64.b64encode(raw_text.encode()).decode()
#     new_filename = f"new_text_file_{timestr}.txt"

#     # Using HTML to style and reduce space between texts
#     download_text_html = f"""
#     <p style='margin:0;padding:0;'><b>Download File</b></p>
#     <p style='margin:0;padding:0;'><a href="data:file/txt;base64,{b64}" download="{new_filename}">Click Here!!</a></p>
#     """
#     st.markdown(download_text_html, unsafe_allow_html=True)



# def csv_downloader(df):
#     csvfile = df.to_csv()
#     b64 = base64.b64encode(csvfile.encode()).decode()
#     new_filename = f"new_csv_file_{timestr}.csv"

#     # Using HTML to style and reduce space between texts
#     download_csv_html = f"""
#     <p style='margin:0;padding:0;'><b>Download File</b></p>
#     <p style='margin:0;padding:0;'><a href="data:file/csv;base64,{b64}" download="{new_filename}">Click Here!!</a></p>
#     """
#     st.markdown(download_csv_html, unsafe_allow_html=True)



### Class Approach (you can also decide to make the filename an input too)
class download_file:
    def __init__(self,data,type):
        self.data = data
        self.type = type
    
    def file_download(self):
        if self.type == 'csv':
            self.data = self.data.to_csv() # or self.data.to_csv(index=False)
        b64 = base64.b64encode(self.data.encode()).decode()
        new_filename = f"new_text_file_{timestr}.{self.type}"

        # Using HTML to style and reduce space between texts
        download_text_html = f"""
        <p style='margin:0;padding:0;'><b>Download File</b></p>
        <p style='margin:0;padding:0;'><a href="data:file/{self.type};base64,{b64}" download="{new_filename}">Click Here!!</a></p>
        """
        st.markdown(download_text_html, unsafe_allow_html=True)


def main():

    menu = ["Home", "CSV", "About"]
    choice  =  st.sidebar.selectbox("Menu", menu)

    st.title("File Downloads")

    if choice == "Home":
        my_text = st.text_area("Your message")

        if st.button("save"):
            st.write(my_text)
            text_downloader = download_file(my_text,'txt')
            text_downloader.file_download()
        
    elif choice == "CSV":
        df = pd.read_csv("iris.csv")
        st.dataframe(df)
        csv_downloader = download_file(df,'csv')
        csv_downloader.file_download()
            
    else:
        st.subheader("About")


    k=5
    if k<10:
        take_screenshoot_and_save()
        st.success("Screenshot taken successfully")

    
if __name__ == '__main__':
    main()