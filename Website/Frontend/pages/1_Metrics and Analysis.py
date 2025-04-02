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
train_stats_path = f"{Path(__file__).parent.parent.parent.parent}/Data/Filtered_Feeders_Metadata/Train_Stats"

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


def get_metrics_from_path_based_on_time_type(feeder_metrics_path, time_type):
    if time_type == "Daytime":
        feeder_metrics_path = feeder_metrics_path + "/Daytime"
    elif time_type == "Nighttime":
        feeder_metrics_path = feeder_metrics_path + "/Nighttime"
    elif time_type == "Overall":
        feeder_metrics_path = feeder_metrics_path + "/Overall"
    else:
        raise ValueError("Invalid time_type. Choose either 'Daytime' or 'Nighttime'.")
    return feeder_metrics_path


def get_train_stats_from_path_based_on_time_type(train_stats_path, time_type):
    if time_type == "Daytime":
        train_stats_path = train_stats_path + "/Daytime"
    elif time_type == "Nighttime":
        train_stats_path = train_stats_path + "/Nighttime"
    else:
        raise ValueError("Invalid time_type. Choose either 'Daytime' or 'Nighttime'.")
    return train_stats_path


def get_feeder_metrics_from_path(feeder_metrics_path, feeder_save_name):
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

    return combined_metrics


for i in range(feeders_metadata.shape[1]):
    feeder = feeders_metadata.iloc[i]
    feeder_name = feeder["FeederName"]
    feeder_capacity = feeder["Capacity"]
    feeder_save_name = feeder["FileSaveName"]
    daytime_feeder_metrics_path = get_metrics_from_path_based_on_time_type(feeder_metrics_path, "Daytime")
    nighttime_feeder_metrics_path = get_metrics_from_path_based_on_time_type(feeder_metrics_path, "Nighttime")
    overall_feeder_metrics_path = get_metrics_from_path_based_on_time_type(feeder_metrics_path, "Overall")
    daytime_train_stats_path = get_train_stats_from_path_based_on_time_type(train_stats_path, "Daytime")
    nighttime_train_stats_path = get_train_stats_from_path_based_on_time_type(train_stats_path, "Nighttime")

    daytime_feeder_metrics = get_feeder_metrics_from_path(daytime_feeder_metrics_path, feeder_save_name)
    nighttime_feeder_metrics = get_feeder_metrics_from_path(nighttime_feeder_metrics_path, feeder_save_name)
    overall_feeder_metrics = get_feeder_metrics_from_path(overall_feeder_metrics_path, feeder_save_name)

    st.header(feeder_name)
    st.subheader(f"Capacity: {feeder_capacity} kW")

    st.subheader("Daytime Metrics")
    st.dataframe(daytime_feeder_metrics, width=500)

    st.subheader("Nighttime Metrics")
    st.dataframe(nighttime_feeder_metrics, width=500)

    st.subheader("Overall Metrics")
    st.dataframe(overall_feeder_metrics, width=500)

    # st.dataframe(feeder_val_metrics, width=500)
    # st.dataframe(feeder_test_metrics, width=500)
    # st.dataframe(combined_metrics, width=500)
