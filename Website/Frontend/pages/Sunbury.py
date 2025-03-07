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

page_title = "Sunbury"
file_name = "Sunbury_HA2B2"

display_page_component(page_title, file_name)
