import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import os

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "movies.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "movie.csv")

st.title("Dashboard - Comicbook Adapted Movie")

st.subheader("Perfomance of rival movies")

img = image.imread(IMAGE_PATH)
st.image(img)

st.subheader("Perfomance of rival movies")

df = pd.read_csv(DATA_PATH)
st.dataframe(df)

option = st.selectbox('Which parameter would you like to use?', ('Metascore', 'Rate'))

st.bar_chart(df, x='Original Title', y=option, use_container_width=True)