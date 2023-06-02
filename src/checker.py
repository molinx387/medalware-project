import pandas as pd
from malware_definitions import malware_dict

df = pd.read_csv("src/data/malwares.csv")
malware_list = df["Malware"].unique()

for malware in malware_list:
    found = False
    for malware_dict in malware_dict:
        if malware == malware_dict["Malware"]:
            found = True
            break
    if not found:
        print(f"{malware} no se encuentra en ninguna llave Malware.")
