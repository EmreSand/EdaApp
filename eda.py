import numpy as np
import pandas as pd
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

#  Title of Web App
st.markdown(''' # **EDA App** 
            This is a simple **EDA App**
            **Streamlit** and **pandas-profiling** library have been utilized to create this app
            
            ''')

# CSV data uploading
with st.sidebar.header("1. Upload your CSV file"):
    uploaded_file = st.sidebar.file_uploader("Upload your CSV data file", type=["csv"])
    st.sidebar.markdown('''
                        [Example CSV data file] (my github link with credit to the original author))
                        ''')

# Pandas Profiling
if uploaded_file: # is not None necessary????
    @st.cache_data
    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    df = load_csv()
    pr = ProfileReport(df, explorative=True)
    st.header("***Input DataFrame***")
    st.write(df)
    st.write("---")
    st.header("***Pandas Profiling Report***")
    st_profile_report(pr)


