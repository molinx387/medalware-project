import json                 
import requests
import csv
import pandas as pd
url = "https://mb-api.abuse.ch/api/v1/"
headers = { 'API-KEY' : '5f93b4ae1962f1fb2c5f67735401f6f3'}
data = { 'query' : 'get_recent', 'selector':'100'}

def recent_malware(url,data, headers):
    malware_data = list()    
    response = requests.post(url, data=data, timeout=15,
                              headers=headers, allow_redirects=True)
    malwares = response.json()
    for malware in malwares['data']:
        malware_sha = malware['sha256_hash'] 
        data_sha = { 'query' : 'get_info', 'hash':malware_sha}
        response_sha = requests.post(url, data=data_sha, timeout=15,
headers=headers, allow_redirects=True)
        if response_sha.json()["query_status"] == 'hash_not_found':
            print('>>>>>>>>>>  The sample hash was not found on Malbazaar <<<<<<<<<<')
        else:
        response_json = response_sha.json()
            for sha_data in response_json["data"]:
                listing_sha = [ sha_data["sha256_hash"], sha_data['signature'], 
                   sha_data['file_type'], sha_data['file_size'],
                   sha_data['delivery_method'],sha_data['origin_country'],
                   sha_data['first_seen'],sha_data['yara_rules'],
                   sha_data['vendor_intel']]
                malware_data.append(listing_sha)
    csvheader = ['SHA256','Familia','Tipo Archivo','cantidad',
                 'Metodo de Entrega','Origen','Fecha', 'Hora',
                 'REGLAS YARA','INFORMES EXTERNOS']
    with open('detections.csv','w',encoding='UTF8', newline='') as f: 
        writter = csv.writer(f)
        writter.writerow(csvheader)
        writter.writerows(malware_data)
    df = pd.DataFrame(malware_data)
    return(pd)
recent_malware(url=url,data=data,headers=headers)
