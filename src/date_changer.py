import pandas as pd 
from malware_definitions import malware_dict
df = pd.read_csv("src/data/malwares.csv")


for dictionary in malware_dict:
    # Check if the value of the key "Nombre" is in the Malware column of the dataframe
    mask = df['Malware'] == dictionary['Malware']
    if mask.any():
        # Update the values in the "Familia" column where the condition is True
        df.loc[mask, 'Familia'] = dictionary['Familia']
        df.loc[mask, 'SO'] = dictionary['SO']
    else: 
        df.loc[mask, 'Familia'] = 'Desconocida'
        df.loc[mask, 'SO'] = 'Desconocido'


df.to_csv('src/data/malwares.csv', index=False)
