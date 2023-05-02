import pandas as pd


def cleaner():
    df = pd.read_csv(open("src/data/example.csv"), index_col=0)
    df["Fecha"] = pd.to_datetime(df["Fecha"])
    df["Dia"] = [d.date() for d in df["Fecha"]]
    df["Hora"] = [d.time() for d in df["Fecha"]]
    df["Metodo de Entrega"].fillna("Desconocido", inplace=True)
    df.dropna(inplace=True)
    df.to_csv("src/data/example.csv")


if __name__ == "__main__":
    cleaner()
