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


page_title = "Swan Street"
file_name = "Swan_Street_TY2B6"

display_page_component(page_title, file_name)


# st.set_page_config(
#     page_title=page_title, page_icon="📊", layout="wide"  # Optional: adds an icon to the browser tab  # Optional: makes the layout wide
# )
# st.title(page_title)


# current_dir = Path(__file__).parent

# train_file_path = f"{current_dir.parent.parent.parent}/Results/{file_name}/{file_name}_train_results.csv"
# val_file_path = f"{current_dir.parent.parent.parent}/Results/{file_name}/{file_name}_val_results.csv"
# test_file_path = f"{current_dir.parent.parent.parent}/Results/{file_name}/{file_name}_test_results.csv"


# def display_results(file_path):
#     # Check if the file exists
#     if os.path.exists(file_path):
#         data = pd.read_csv(file_path, index_col="Time")
#         data = data[["Actual", "RLS", "LSTM", "ANN"]]
#         fig = px.line(data)
#         fig.show()
#         st.plotly_chart(fig)

#         return data
#     else:
#         st.write("File not found.")
#         st.write(file_path)

# st.header("Train Results")
# results_train = display_results(train_file_path)
# st.subheader("Values")
# st.dataframe(results_train)

# st.header("Validation Results")
# results_val = display_results(val_file_path)
# st.subheader("Values")
# st.dataframe(results_val)

# st.header("Test Results")
# results_test = display_results(test_file_path)
# st.subheader("Values")
# st.dataframe(results_test)
