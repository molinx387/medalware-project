import streamlit as st
import json                 
import requests
import pandas as pd
import numpy as np
import csv  
import matplotlib.pyplot as plt

#Inicio de App
st.title('👾MEDALWARE APLICATION👾')
st.text('MEDALWARE is a web application developed to display information through\nEDA techniques(Exploratory Data Analysis) related to malware samples\nfrom the MalwareBazaar site.The purpose of this app is to provide \ninformation about threats,identifying new trends and patterns.')

st.header(' 📈 Historic Data ')

url = "https://mb-api.abuse.ch/api/v1/"
API_KEY = '5f93b4ae1962f1fb2c5f67735401f6f3' 

#Connect to the API
headers = { 'API-KEY' : '5f93b4ae1962f1fb2c5f67735401f6f3'}
data = { 'query' : 'get_recent', 'selector':'100'}
response = requests.post(url, data=data, timeout=15, headers=headers, allow_redirects=True)
malwares = response.json()

#Taking the data from the jsooooon
topics_malware = [] 
csvheader = ["FIRST SEEN","FILE TYPE","COUNTRY","TAGS","SIZE","SIGNATURE"]
for malware in malwares['data']:
    listing = [malware['first_seen'], malware['file_type'],malware['origin_country'],malware['tags'],malware['file_size'],malware['signature']]
    topics_malware.append(listing)
with open('detections.csv','w',encoding='UTF8', newline='') as f: 
    writter = csv.writer(f)
    writter.writerow(csvheader)
    writter.writerows(topics_malware) 

df= pd.read_csv('C:/Users/Admin/Desktop/PRUEBAS/detections.csv')
st.dataframe(df)
st.header(' 📈 Historic Data Flow ')
st.bar_chart(data=df, x='COUNTRY', y='SIZE', width=1000, height=250, use_container_width=False)
st.line_chart(data=df, x='TAGS', y='SIZE', width=100, height=500, use_container_width=True)
#   st.area_chart(data=df, x='TAGS', y='SIZE', width=5000, height=5000, use_container_width=True)

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
st.pyplot(fig1)