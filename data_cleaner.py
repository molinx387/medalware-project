import pandas as pd
import numpy as np
import csv  
import matplotlib.pyplot as plt
import streamlit as st

data_set = 'C:/Users/Admin/Documents/M/MEDALWARE-PROJECT/detections_data.csv'
data = pd.read_csv(data_set)

print(data.shape)
print(data.info())
data.dropna(inplace=True)
print(data.info())