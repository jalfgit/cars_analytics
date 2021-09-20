data_path='./data/'
data_file = 'cars.csv'

import pandas as pd
import numpy as np
import streamlit as st
from streamlit.proto.RootContainer_pb2 import SIDEBAR

cars=pd.read_csv(data_path+data_file)

st.title('Cars Modeling')
st.header('Random Forest Regressor Model')

st.sidebar.header('Input Components')
st.sidebar.text('Area to input model parameters')

st.dataframe(cars[0:10])

def graph_data():
    st.bar_chart(cars.groupby('brand').sum()['price'])

graph_this = st.sidebar.button("Graph Data?")
if graph_this:
    graph_data()