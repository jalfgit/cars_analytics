# actual library that holds the model to predict

import numpy as np
# import matplotlib.pyplot as plt
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error,f1_score


# adding pre-processing to scale data which is inherent in the Pipeline in the pyspark done earlier
from sklearn.preprocessing import StandardScaler,MinMaxScaler


# saving model library
import pickle

# access settings
data_path='./data/'
data_file = 'cars.csv'
model_file='./models/rfr.sav'

def load_data():
    # assume data file will always be the same per training
    df = pickle.load(open(data_path+'cars.pkl', 'rb'))
    return df

def load_model(model_file_name):
    loaded_model = pickle.load(open(model_file_name, 'rb'))
    return loaded_model

def brand_converter(df,brand):
    brand_matrix = pd.get_dummies(df['brand']).drop_duplicates().set_index(pd.get_dummies(df['brand']).drop_duplicates().columns)
    return brand_matrix.loc[brand].tolist()

def color_converter(df,color):
    color_matrix = pd.get_dummies(df['color'].sort_values()).drop_duplicates().set_index(pd.get_dummies(df['color']).drop_duplicates().columns)
    return color_matrix.loc[color].tolist()

def predict_worth(car:list):
    rfr_m = load_model(model_file)
    car_value = rfr_m.predict([car,])
    return car_value