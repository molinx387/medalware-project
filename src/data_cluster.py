import os
import pandas as pd
from data_cleaner import cleaner


def cluster():
    df1 = cleaner()
    df2 = pd.read_csv("src/data/malwares.csv")

    if os.path.isfile(os.path.join("./data/", "malwares.csv")):
        for index, row in df1.iterrows():
            if not df2.isin(row).any().any():
                df2 = df2.append(row)
        df2.to_csv("src/data/malwares.csv")
    else:
        df1.to_csv("src/data/malwares.csv")


cluster()
# df.to_csv('my_csv.csv', mode='a', header=False)
