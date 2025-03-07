import numpy as np
import streamlit as st
from pathlib import Path
import pandas as pd
import plotly.express as px
import plotly.io as pio
from plotly import graph_objects as go
import plotly.express as px
import os
from utils.page_component import display_page_component

page_title = "Analysis"
file_name = "Chapel_Street_TY2B4"
current_dir = Path(__file__).parent
feeder_stats_path = f"{Path(__file__).parent.parent.parent.parent}/Data/Filtered_Feeders_Metadata/Feeder_Stats.csv"
feeders_metadata_path = (
    f"{Path(__file__).parent.parent.parent.parent}/Data/Filtered_Feeders_Metadata/Final_Selected_Feeders_Data_with_Coordinates.csv"
)
feeder_metrics_path = f"{Path(__file__).parent.parent.parent.parent}/Results/Metrics"

feeder_stats = pd.read_csv(feeder_stats_path)
feeder_stats.index.name = "index"

feeders_metadata = pd.read_csv(feeders_metadata_path)

st.set_page_config(
    page_title=page_title, page_icon="📊", layout="wide"  # Optional: adds an icon to the browser tab  # Optional: makes the layout wide
)

st.title(page_title)

st.header("Statistics")
st.markdown("The following table describes the distribution of Net Load Demand for each feeder.")
st.dataframe(feeder_stats)

st.title("Metrics")
st.markdown("Train, Validation and Test metrics for Actual vs Predictions of normalized Net Load Demand for each feeder.")
st.subheader("Metrics Used: ")
st.markdown("RMSE - Root Mean Squared Error")
st.markdown("MAE - Mean Absolute Error")
st.markdown("SMAPE - Symmetric Mean Absolute Percentage Error")

for i in range(feeders_metadata.shape[1]):
    feeder = feeders_metadata.iloc[i]
    feeder_name = feeder["FeederName"]
    feeder_save_name = feeder["FileSaveName"]
    feeder_metrics = pd.read_csv(f"{feeder_metrics_path}/{feeder_save_name}_Metrics.csv")
    feeder_metrics.rename(columns={"Unnamed: 0": "Metric"}, inplace=True)
    # feeder_metrics.index.name = "Metric"

    st.header(feeder_name)
    st.dataframe(feeder_metrics, width=500)
