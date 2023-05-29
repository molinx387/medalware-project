import pandas as pd 
from malware_definitions import malware_dict

df = pd.read_csv("src/data/malwares.csv")
df['Fecha'] = pd.to_datetime(df.pop('Dia')) + pd.to_timedelta(df.pop('Hora'))
df.rename(columns = {'Familia':'Malware'}, inplace=True)
df.rename(columns = {'Peso (MB)':'Peso'}, inplace=True)
df.insert(0,"Familia", " ")
df.insert(0,"Sistema Operativo", " ")

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

df = df.reindex(columns=['Fecha', 'SHA256', 'Malware',
                         'Familia', 'Sistema Operativo',
                         'Metodo de Entrega','Extension',
                         'Peso','Origen'])

df.to_csv('src/data/malwares.csv', index=False)
