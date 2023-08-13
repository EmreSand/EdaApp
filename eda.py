import numpy as np
import pandas as pd
import streamlit as st
# from pandas_profiling import ProfileReport
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

#  Title of Web App
st.markdown('''  **EDA App** 
            This is a simple **EDA App**
            **Streamlit** and **pandas-profiling** library have been utilized to create this app
            
            ''')

# CSV data uploading
with st.sidebar.header("1. Upload your CSV file"): # Sidebar panel 
    uploaded_file = st.sidebar.file_uploader("Upload your CSV data file", type=["csv"])
    st.sidebar.markdown('''
                        [Example CSV data file] 
                        ''')

# Pandas Profiling
if uploaded_file:  # Profiling with the data user input

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

else:

    st.info("Awaiting for CSV file upload")
    if st.button("Press to use Example Dataset"): # User can prefer example data here

        @st.cache_data
        def load_data():  # A function to create a sample DataFrame of size 100*5 and random numbers between 0-1
            sample = pd.DataFrame(
                np.random.rand(100,5), 
                columns=['a', 'b', 'c', 'd', 'e']
            )
            return sample
        df = load_data()
        pr = ProfileReport(df, explorative=True)
        st.header("***Input DataFrame***")
        st.write(df)
        st.write("---")
        st.header("*** Pandas Profiling Report***")
        st_profile_report(pr) # Displaying Profile Report

