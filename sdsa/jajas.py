import streamlit as st
import json                 
import requests
import pandas as pd
import numpy as np
import csv  
import matplotlib.pyplot as plt


"""#Inicio de App
st.title('👾MEDALWARE APLICATION👾')
st.text('MEDALWARE is a web application developed to display information through\nEDA techniques(Exploratory Data Analysis) related to malware samples\nfrom the MalwareBazaar site.The purpose of this app is to provide \ninformation about threats,identifying new trends and patterns.')
st.header(' 📈 Historic Data ')
"""


url = "https://mb-api.abuse.ch/api/v1/"
API_KEY = '5f93b4ae1962f1fb2c5f67735401f6f3' 

#Connect to the API
headers = { 'API-KEY' : '5f93b4ae1962f1fb2c5f67735401f6f3'}
data = { 'query' : 'get_recent', 'selector':'100'}
response = requests.post(url, data=data, timeout=15, headers=headers, allow_redirects=True)
malwares = response.json()

#Taking the data from the jsooooon
topics_malware = [] 
csvheader = ["FIRST SEEN","FILE TYPE","COUNTRY","SIZE","SIGNATURE","SHA256"]
for malware in malwares['data']:
    listing = [malware['first_seen'], malware['file_type'],malware['origin_country'],
               malware['file_size'],malware['signature'], malware["sha256_hash"]]
    topics_malware.append(listing)
with open('detections.csv','w',encoding='UTF8', newline='') as f: 
    writter = csv.writer(f)
    writter.writerow(csvheader)
    writter.writerows(topics_malware) 

file_malware = open('detections.csv')
csvreader = csv.reader(file_malware)
sha256_list = []

for row in csvreader:
    sha256_list.append(str(row[5]))

del(sha256_list[0])
ayuda = []
invento = [] 
for shash in sha256_list:
    data_sha = { 'query' : 'get_info', 'hash':shash}
    invento.append(data_sha)
    
for every in invento:
    response_sha = requests.post(url, data=every, timeout=15, headers=headers, allow_redirects=True)
    response_json = response_sha.json()["data"][0]
    for element in response_json:
        listed_element =[element[response_json.get("delivery_method")],
                                  element[response_json.get("yara_rules")],
                                  element[response_json.get("vendor_intel")]]
    ayuda.append(listed_element)


csvheader_sha = ["DELIVERY METHOD","YARA RULES","VENDOR INTEL"]
with open('detections_sha.csv','w',encoding='UTF8', newline='') as c: 
    writter = csv.writer(c)
    writter.writerow(csvheader_sha)
    for item in ayuda:
         writter.writerow([item])

df1 = pd.read_csv('detections.csv')
df2 = pd.read_csv('detections_sha.csv')

concatenated = pd.concat([df1, df2], axis=1, ignore_index=False)

concatenated.to_csv('detections_data.csv', index=False)
"""
df= pd.read_csv('detections.csv')
st.dataframe(df)
st.header(' 📈 Historic Data Flow ')
st.bar_chart(data=df, x='COUNTRY', y='SIZE', width=1000, height=250, use_container_width=False)
#st.line_chart(data=df, x='TAGS', y='SIZE', width=100, height=500, use_container_width=True)
# st.area_chart(data=df, x='TAGS', y='SIZE', width=5000, height=5000, use_container_width=True)
"""


