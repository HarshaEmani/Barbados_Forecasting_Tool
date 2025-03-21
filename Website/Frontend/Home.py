import numpy as np
import streamlit as st
from pathlib import Path
import pandas as pd
import plotly.express as px
import plotly.io as pio
from plotly import graph_objects as go

architecture_image_path = Path(__file__).parent / "images" / "Architecture.png"

st.set_page_config(page_title="Barbados Forecasting Tool", layout="wide")
st.title("Barbados Forecasting Tool")

st.subheader("Architecture")
st.image(architecture_image_path)

st.subheader("Methodology")
st.markdown("This tool uses a combination of Deep Learning methods to generate day-ahead forecasts for the time series data for different feeders in Barbados.")
st.markdown("Steps: ")
st.markdown("1. Data Preprocessing")
st.markdown("2. Weather Features Extraction")
st.markdown("3. Optimal Feature Selection")
st.markdown("4. Feature Engineering")
st.markdown("5. Data Normalization")
st.markdown("6. Data Combination")
st.markdown("7. Data Splitting - Training, Validation, Test sets")
st.markdown("8. Model Training on Training Set")
st.markdown("9. Model Forecasting on Validation and Test Sets")
st.markdown("10. Model Evaluation and Tuning")


# st.subheader("Training")
# st.markdown("For a given feeder: ")
# st.markdown("1. The data is retreived from a specified location.")
# st.markdown("2. The raw data is cleaned, preprocessed and resampled to 1 hour resolution")
# st.markdown("3. The processed data is combined with weather data for the feeder's location.")
# st.markdown("4. Feature Selection is performed to select the best predictors. The following features were selected for training: 'Temperature', 'Cloud Cover', 'Shortwave Radiation'")
# st.markdown("5. Feature Engineering is performed to create new features from the selected predictors, such as 'Day of Week', 'Is Holiday' and added to the matrix of predictors.")
# st.markdown("6. Every signal is normalized before creation of matrix of predictors.")
# st.markdown("7. Each row of the features matrix represents: 24 samples each for historic values and forecasted values of 'Temperature', 'Cloud Cover', 'Shortwave Radiation', One Hot encoded values of 'Day of Week', 'Is Holiday' and 24 samples of historic values for previous day's Net Load Demand.")
# st.markdown("8. Each row of the target matrix represents: 24 samples of observed Net Load Demand for the forecasted day.")
# st.markdown("9. The data is split into training, validation and test sets.")
# st.markdown("10. Two deep learning models are trained on the training set: ANN and LSTM.")
# st.markdown("11. Each model has 2 sub-models which train on base load and change in load simultaneously.")
# st.markdown("12. The trained ANN and LSTM models are seperately combined using an RLS Combiner, by converting the change in load to base load and combining the forecasts.")
# st.markdown("11. Another RLS Combiner Model is used to combine the forecasts from the two models to predict the optimal forecasts and learn from both models.")
# st.markdown("12. The trained models of ANN, LSTM for Base Load and Change in Load and RLS Combiners are saved for future use.")

# st.subheader("Forecasting")
# st.markdown("1. The data is retreived from a specified location.")
# st.markdown("2. The raw data is cleaned, preprocessed and resampled to 1 hour resolution, and combined with weather data for the feeder's location using the same methods used for training.")
# st.markdown("3. The saved models are loaded and used to forecast the Net Load Demand for the validation and test sets.")
# st.markdown("4. The forecasting architecture is similar to the training process, where two deep learning models (ANN and LSTM) are initially used to generate forecasts and finally combined by a Recursive Lease Squares Combiner.")
# st.markdown("5. The generated forecasts are saved and used for analysis.")

st.subheader("Assumptions and Future Work")
st.markdown("1. The data sent to models is assumed to be clean and preprocessed and sampled to 1 hour resolution.")
st.markdown("2. The weather data is assumed to be accurate and reliable. ")
st.markdown("3. The data is currently limited and only available from 1st January 2024 to 31st July 2024. For some feeders, the data is limited to 1st March 2024 to 30th June 2024. As more data becomes available, the tool will be updated to include the new data.")
st.markdown("4. The Training data spans until the end of May, Validation data spans from end of training data until the end of June. The remaining data is used for testing.")
st.markdown("5. As real-time data becomes available, the tool will be automated to generate forecasts for the real-time data, with an automated process running everyday.")
st.markdown("6. On some days, the additional data is missing for some feeders. The tool will be updated to handle missing data in the future. Additional information like sudden spikes and sudden drops in actual net load demand, etc. will be used to improve the forecasting accuracy.")
st.markdown("7. The tool is currently limited to day ahead forecasting. The tool was built dynamically to be easy to update the forecast horizon for few hours ahead or multiple days ahead based on requirement and data availability. The models will need to be retrained for different forecast horizons.")
st.markdown("8. The following quality attributes were prioritized at the time of building this tool: 'Reliability', 'Maintainability', 'Usability' and 'Scalability'.")

st.subheader("Contributors")
st.markdown("1. **Harsha Emani** - *MLOps Engineer, Gradudate Research Assistant, University of New Brunswick*")
st.markdown("2. **Dr. Julian Cardenas Barrera** - *Associate Professor, ECE Department, University of New Brunswick*")

# st.sidebar.markdown("# Barbados Forecast")

# st.markdown("Green Hill")
# st.write("Hello, World!")

# current_dir = Path(__file__).parent

# # # Construct the absolute path to the CSV file
# green_hill_train_val_test_path = "green_hill_train_val_test_data.json"
# green_hill_naive_forecast_path = "green_hill_naive_forecast.json"
# green_hill_baseline_no_exogenous_forecast_path = "green_hill_baseline_no_exogenous_forecast.json"
# green_hill_baseline_exogenous_forecast_path = "green_hill_baseline_exogenous_forecast.json"
# green_hill_baseline_exogenous_probablistic_forecast_path = "green_hill_baseline_exogenous_probablistic_forecast.json"

# green_hill_train_val_test_fig = current_dir.parent.parent / "Plots" / green_hill_train_val_test_path
# green_hill_naive_forecast_fig = current_dir.parent.parent / "Plots" / green_hill_naive_forecast_path
# green_hill_baseline_no_exogenous_forecast_fig = current_dir.parent.parent / "Plots" / green_hill_baseline_no_exogenous_forecast_path
# green_hill_baseline_exogenous_forecast_fig = current_dir.parent.parent / "Plots" / green_hill_baseline_exogenous_forecast_path
# green_hill_baseline_exogenous_probablistic_forecast_fig = current_dir.parent.parent / "Plots" / green_hill_baseline_exogenous_probablistic_forecast_path

# green_hill_train_val_test_loaded_fig = pio.read_json(green_hill_train_val_test_fig)
# green_hill_naive_forecast_loaded_fig = pio.read_json(green_hill_naive_forecast_fig)
# green_hill_baseline_no_exogenous_forecast_loaded_fig = pio.read_json(green_hill_baseline_no_exogenous_forecast_fig)
# green_hill_baseline_exogenous_forecast_loaded_fig = pio.read_json(green_hill_baseline_exogenous_forecast_fig)
# green_hill_baseline_exogenous_probablistic_forecast_loaded_fig = pio.read_json(green_hill_baseline_exogenous_probablistic_forecast_fig)

# #
# # # # Read the CSV file using the absolute path
# # df = pd.read_csv(csv_path, index_col=0)
# # df.index = pd.to_datetime(df.index)
# #
# # df['actual'][-15:] = None
# #
# # # st.dataframe(df)
# #
# # fig = px.line(df, x=df.index, y=['actual', 'prediction'])
# # # Set the default zoom level by specifying axis ranges
# # fig.update_layout(
# #     xaxis=dict(range=[df.index[-30], df.index[-1]]),  # Adjust as needed
# #     # yaxis=dict(range=[df['y_column_name'].min(), df['y_column_name'].max()])  # Adjust as needed
# # )
# #
# # # fig.show()
# # # fig.show()
# #
# st.plotly_chart(green_hill_train_val_test_loaded_fig)
# st.plotly_chart(green_hill_naive_forecast_loaded_fig)
# st.plotly_chart(green_hill_baseline_no_exogenous_forecast_loaded_fig)
# st.plotly_chart(green_hill_baseline_exogenous_forecast_loaded_fig)
# st.plotly_chart(green_hill_baseline_exogenous_probablistic_forecast_loaded_fig)
