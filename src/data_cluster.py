import os
import pandas as pd
from data_cleaner import cleaner


def cluster():
    df1 = cleaner()
    if os.path.exists("malwares.csv") == False:
        df2 = df1
        df2.to_csv("src/data/malwares.csv", index=False)
    else:
        df2 = pd.read_csv("src/data/malwares.csv", index_col=[0])
        df3 = pd.concat([df1, df2], ignore_index=True).drop_duplicates()
        df3.to_csv("src/data/malwares.csv", index=True)
    return


if __name__ == "__main__":
    cluster()
