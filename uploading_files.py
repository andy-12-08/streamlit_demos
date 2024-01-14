import streamlit as st
from PIL import Image  #for loading images
import pandas as pd
import pdfplumber
import docx2txt
import os

st.set_page_config(initial_sidebar_state="expanded")

## Some pre-defined functions

#load images into a function using pillow
def load_image(image_file):
    img = Image.open(image_file)
    return img

#Save files to temp directory
def save_uploaded_file(uploadedfile):
    with open(os.path.join('temp',uploadedfile.name),'wb') as f:
        f.write(uploadedfile.getbuffer())
    return st.success(f'saved file: {uploadedfile.name} in temp')


menu = ("Home","Dataset", "DocumentFiles", "About")
choice = st.sidebar.selectbox("Menu", menu)

st.title('File Upload Tutorial')

## Handle single image

#if choice == 'Home':
#    st.subheader('Home')
#    image_file = st.file_uploader("Upload Images", type = ["png", 'jpg', 'jpeg'])
#    if image_file is not None:
#        image_details = {"filename": image_file.name,
#                         "filetype":image_file.type,
#                         "filesize": image_file.size}
#        st.write(image_details)
#        st.image(load_image(image_file))
#        save_uploaded_file(image_file)
#

## To handle multiple images
if choice == 'Home':
    st.subheader('Home')
    image_file = st.file_uploader("Upload Images", type = ["png", 'jpg', 'jpeg'], accept_multiple_files=True)
    if image_file is not None:     # the image_file is now a ByteIO list 
        for image in image_file:
            image_details = {"filename": image.name,
                            "filetype":  image.type,
                            "filesize":  image.size}
            st.write(image_details)
            st.image(load_image(image), width=250)
            save_uploaded_file(image)

## Handle csv files    
elif choice == 'Dataset':
    st.subheader('Dataset')
    data_file = st.file_uploader("Upload CSV", type = ['csv'])
    if data_file is not None:
        data_details = {"filename": data_file.name,
                         "filetype": data_file.type,
                         "filesize": data_file.size}
        st.write(data_details)
        df = pd.read_csv(data_file)
        st.dataframe(df)
        save_uploaded_file(data_file)


## Handle pdfs, docx and txt
elif choice == 'DocumentFiles':
    st.subheader('DocumentFiles')
    docx_file = st.file_uploader("Upload Doc.", type=['pdf','docx','txt'])
    if st.button('Process'):   # add a process button
        if docx_file is not None:    
            docx_details = {"filename": docx_file.name,
                            "filetype": docx_file.type,
                            "filesize": docx_file.size}
            st.write(docx_details)  #output file details
            if docx_file.type == "text/plain":     #processing txt
                raw_text = str(docx_file.read(), "utf-8")
                st.write(raw_text)
            elif docx_file.type == "application/pdf":   #processing pdfs
                # catch any errors
                try:
                    with pdfplumber.open(docx_file) as pdf:
                        pages = pdf.pages[0]
                        st.write(pages.extract_text())
                except:
                    st.write("None")
            #use docx2txt to open docx
            else:
                raw_text = docx2txt.process(docx_file)
                st.write(raw_text)

else:
    st.subheader('About')