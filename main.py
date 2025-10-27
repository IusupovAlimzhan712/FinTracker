import streamlit as st
import pandas as pd
import plotly.express as px
import json
import os

st.set_page_config("FinTracker", "💰", "wide")


def load_transuctions(uploaded_file):
    try:
        df = pd.read_csv(uploaded_file)
        df.index = range(1, len(df) + 1)
        df.index.name = "No"

        df.columns = [col.strip() for col in df.columns]
      
        df["Date"] = pd.to_datetime(df["Date"], errors="coerce", infer_datetime_format=True)
        df["Date"] = pd.to_datetime(df["Date"]).dt.strftime("%Y-%m-%d %H:%M")


        st.write(df)
        return df
    except Exception as e:
        st.error(f"Error processing file: {str(e)}")
        return None
    

def main():
    st.title("FinTracher Dashboard")
    uploaded_file = st.file_uploader("Upload your transuction CSV file", type = ["csv"])

    if uploaded_file is not None:
        df = load_transuctions(uploaded_file)


main()
