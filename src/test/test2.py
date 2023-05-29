import pandas as pd

df = pd.read_csv("src/test/malwares.csv")
dictionaries = [
    {
        'Nombre': 'Mirai',
        'Familia': 'Botnet',
    }
]
# Iterate through each dictionary in the list
for dictionary in dictionaries:
    # Check if the value of the key "Nombre" is in the Malware column of the dataframe
    mask = df['Malware'] == dictionary['Nombre']
    if mask.any():
        # Update the values in the "Familia" column where the condition is True
        df.loc[mask, 'Familia'] = dictionary['Familia']

df.to_csv('src/test/malwares.csv', index=False)
