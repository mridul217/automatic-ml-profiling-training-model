import streamlit as st
import pandas as pd 
import os

# Import profiling capability
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

# ML Stuff
from pycaret.classification import setup, compare_models, pull, save_model 

with st.sidebar:
    st.image("https://cdn.pixabay.com/photo/2023/02/05/19/05/robot-7770312_1280.jpg")
    st.title("Auto Stream Machine Learning!!!")
    choice = st.radio("navigation",["Upload","Profiling","ML","Download"])
    st.info("this app allows you to build as automated Ml platform using Streamlit, Pandas profiling, Pycaret")

if choice == "Upload":
    st.title("Upoad Your Data for Modelling")
    file = st.file_uploader("Upload Your Dataset Here")
    if file:
        df = pd.read_csv(file, index_col=None)
        # df.to_csv("sourcedata.csv", index=None)
        st.dataframe(df)
        st.button("Save Data", on_click=lambda: df.to_csv("sourcedata.csv", index=False))


# if os.path.exists("sourcedata.csv"):
#     df = pd.read_csv("sourcedata.csv", index_col=None)


if choice == "Profiling":
    st.subheader("Automated Exploratory Data Analysis")
    if "sourcedata.csv" in os.listdir():
        config_file = "my_config.yaml"
        df = pd.read_csv("sourcedata.csv")
        profile_report = ProfileReport(df, config_file=config_file)
        st_profile_report(profile_report)
    else:
        st.warning("Please upload a dataset for profiling in the 'Upload' section.")

# if choice == "Profiling":
#     st.title("Automated Exploratory Data Analysis")
#     profile_report = ProfileReport(df)
#     st_profile_report(profile_report)

if choice == "ML":
    st.subheader("***    Machine learning    ***")
    if "sourcedata.csv" in os.listdir():
        df = pd.read_csv("sourcedata.csv")
    target = st.selectbox("Select your target", df.columns)
    if st.button("Train Model"):
        setup(df, target=target, verbose = False)
        setup_df = pull()
        st.info("this is ML Experiment settings")
        st.dataframe(setup_df)
        best_model = compare_models()
        compare_df = pull()
        st.info("This is the ML Model")
        st.dataframe(compare_df)
        best_model
        save_model(best_model,"best_model")


if choice == "Download":
    st.subheader("***    Download the trained model in one click    ***")
    with open ("best_model.pkl", "rb") as f:
        st.download_button("Download the model", f, "trained_model.pkl")