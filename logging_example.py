#core packages
import streamlit as st

# Utils
import logging

# log to terminal
# # FORMAT
# LOGS_FORMAT = "%(levelname)s %(asctime)s.%(msecs)03d %(message)s"
# # create a logger
# logging.basicConfig(level=logging.DEBUG, format=LOGS_FORMAT)
# logger = logging.getLogger(__name__)

# Save to file
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# Formatter 
formatter = logging.Formatter("%(levelname)s %(asctime)s.%(msecs)03d %(message)s")
# File
file_handler = logging.FileHandler('activity.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def main():
    st.title("Adding logs to Apps")
    st.text("Track all activities/pages visited in the app")

    menu = ["Home", "EDA", "ML", "About"]
    choice  =  st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home Section")
        logger.info("Home Section")

    elif choice == "EDA":
        st.subheader("EDA Section")
        logger.info("EDA Section")

    elif choice  == "ML":
        st.subheader("ML Section")
        logger.info("ML Section")
        
    else:
        st.subheader("About")
        logger.info("About Section")

if __name__ == "__main__":
    main()

