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

current_dir = Path(__file__).parent
feeder_stats_path = f"{Path(__file__).parent.parent.parent.parent}/Data/Filtered_Feeders_Metadata/Feeder_Stats.csv"
feeders_metadata_path = (
    f"{Path(__file__).parent.parent.parent.parent}/Data/Filtered_Feeders_Metadata/Final_Selected_Feeders_Data_with_Coordinates.csv"
)
feeder_metrics_path = f"{Path(__file__).parent.parent.parent.parent}/Metrics"

feeder_stats = pd.read_csv(feeder_stats_path)
feeder_stats = feeder_stats.round(2)
feeder_stats.index.name = "index"

feeders_metadata = pd.read_csv(feeders_metadata_path)

st.set_page_config(
    page_title=page_title, page_icon="📊", layout="wide"  # Optional: adds an icon to the browser tab  # Optional: makes the layout wide
)

st.title(page_title)

st.header("Statistics")
st.dataframe(feeder_stats)

st.title("Metrics")
st.markdown("Metrics used:")
st.markdown("- Symmetric Mean Absolute Percentage Error")
st.markdown("- Mean Absolute Error")
st.markdown("- Root Mean Squared Error")

for i in range(feeders_metadata.shape[1]):
    feeder = feeders_metadata.iloc[i]
    feeder_name = feeder["FeederName"]
    feeder_capacity = feeder["Capacity"]
    feeder_save_name = feeder["FileSaveName"]
    feeder_val_metrics = pd.read_csv(f"{feeder_metrics_path}/{feeder_save_name}_Validation_Metrics.csv")
    feeder_val_metrics.rename(columns={"Unnamed: 0": "Metric"}, inplace=True)
    feeder_val_metrics.columns = [f"Validation_{col}" for col in feeder_val_metrics.columns]
    feeder_val_metrics.set_index("Validation_Metric", inplace=True, drop=True)

    feeder_test_metrics = pd.read_csv(f"{feeder_metrics_path}/{feeder_save_name}_Test_Metrics.csv")
    feeder_test_metrics.rename(columns={"Unnamed: 0": "Metric"}, inplace=True)
    feeder_test_metrics.columns = [f"Test_{col}" for col in feeder_test_metrics.columns]
    feeder_test_metrics.set_index("Test_Metric", inplace=True, drop=True)

    combined_metrics = pd.concat([feeder_val_metrics.T, feeder_test_metrics.T], axis=0)
    combined_metrics = combined_metrics.round(2)
    combined_metrics.index.name = "Metric"

    # feeder_metrics.index.name = "Metric"

    st.header(feeder_name)
    st.subheader(f"Capacity: {feeder_capacity}")
    # st.dataframe(feeder_val_metrics, width=500)
    # st.dataframe(feeder_test_metrics, width=500)
    st.dataframe(combined_metrics, width=500)
