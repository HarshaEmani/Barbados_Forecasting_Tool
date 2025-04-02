import numpy as np
import streamlit as st
from pathlib import Path
import pandas as pd
import plotly.express as px
import plotly.io as pio
from plotly import graph_objects as go
import plotly.express as px
import os


def display_results(data):
    fig = px.line(data)
    st.plotly_chart(fig)

    return


def get_results_from_path_and_display(file_path):
    # Check if the file exists
    if os.path.exists(file_path):
        data = pd.read_csv(file_path, index_col=0)
        data = data[["Actual", "ANN_RLS", "LSTM_RLS", "Final_RLS", "Benchmark"]]
        data = data.round(2)

        display_results(data)

        return data
    else:
        st.write("File not found.")
        st.write(file_path)


def display_page_component(page_title, file_name):

    st.set_page_config(
        page_title=page_title, page_icon="📊", layout="wide"  # Optional: adds an icon to the browser tab  # Optional: makes the layout wide
    )
    st.title(page_title)

    current_dir = Path(__file__).parent

    # train_file_path = f"{current_dir.parent.parent.parent}/Results/{file_name}/{file_name}_train_results.csv"
    daytime_val_file_path = f"{current_dir.parent.parent.parent}/Results/Daytime/{file_name}_Validation_Results.csv"
    daytime_test_file_path = f"{current_dir.parent.parent.parent}/Results/Daytime/{file_name}_Test_Results.csv"
    nighttime_val_file_path = f"{current_dir.parent.parent.parent}/Results/Nighttime/{file_name}_Validation_Results.csv"
    nighttime_test_file_path = f"{current_dir.parent.parent.parent}/Results/Nighttime/{file_name}_Test_Results.csv"
    overall_val_file_path = f"{current_dir.parent.parent.parent}/Results/Overall/{file_name}_Validation_Results.csv"
    overall_test_file_path = f"{current_dir.parent.parent.parent}/Results/Overall/{file_name}_Test_Results.csv"

    st.header("Daytime")
    st.header("Test Results")
    daytime_results_test = get_results_from_path_and_display(daytime_test_file_path)
    st.subheader("Test Values")
    st.dataframe(daytime_results_test)

    st.header("Validation Results")
    daytime_results_val = get_results_from_path_and_display(daytime_val_file_path)
    st.subheader("Validation Values")
    st.dataframe(daytime_results_val)

    st.header("Nighttime")
    st.header("Test Results")
    nighttime_results_test = get_results_from_path_and_display(nighttime_test_file_path)
    st.subheader("Test Values")
    st.dataframe(nighttime_results_test)

    st.header("Validation Results")
    nighttime_results_val = get_results_from_path_and_display(nighttime_val_file_path)
    st.subheader("Validation Values")
    st.dataframe(nighttime_results_val)

    st.header("Combined")
    st.header("Test Results")
    overall_results_test = get_results_from_path_and_display(overall_test_file_path)
    st.subheader("Test Values")
    st.dataframe(overall_results_test)

    st.header("Validation Results")
    overall_results_val = get_results_from_path_and_display(overall_val_file_path)
    st.subheader("Validation Values")
    st.dataframe(overall_results_val)

    # st.header("Train Results")
    # results_train = display_results(train_file_path)
    # st.subheader("Train Values")
    # st.dataframe(results_train)
