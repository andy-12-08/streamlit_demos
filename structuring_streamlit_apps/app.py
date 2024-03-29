import streamlit as st

# import mini apps
from eda_app import run_eda_app
from ml_app import run_ml_app


def main():
    st.title("Main App")

    menu = ["Home","EDA", "ML","About"]

    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")

    elif choice == "EDA":
        run_eda_app()
        pass
    
    elif choice == "ML":
        run_ml_app()
        pass

    else:
        st.subheader("About")

if __name__ == "__main__":
    main()