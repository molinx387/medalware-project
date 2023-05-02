import pandas as pd
from data_extractor import recent_malware

def cleaner():
    df = recent_malware()
    df["Fecha"] = pd.to_datetime(df["Fecha"])
    df["Dia"] = [d.date() for d in df["Fecha"]]
    df["Hora"] = [d.time() for d in df["Fecha"]]
    df.drop('Fecha', axis=1, inplace=True)
    df["Metodo de Entrega"].fillna("Desconocido", inplace=True)
    df.dropna(inplace=True)
    df.to_csv("src/data/cleaned.csv")
    return df
 

if __name__ == "__main__":
    cleaner()
