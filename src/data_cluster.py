import os
import pandas as pd
from data_cleaner import cleaner


def cluster():
    df1 = cleaner()
    if os.path.isfile("data/malwares.csv") == False:
        df2 = df1
        df2.to_csv("src/data/malwares.csv")
    else:
        df2 = pd.read_csv("src/data/malwares.csv")
        df3 = pd.concat([df2,df1], ignore_index=True).drop_duplicates()
        df3.to_csv("src/data/malwares.csv", index=True)
    return

if __name__ == "__main__":
    cluster()

