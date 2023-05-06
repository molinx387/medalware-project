import os
import pandas as pd
from data_cleaner import cleaner


def cluster():
    df_recent = cleaner()
    if os.path.isfile("src/data/malwares.csv") == False:
        df_stored = df_recent
        print("NO EXISTE")
        df_stored.to_csv("src/data/malwares.csv", index=False)
    else:
        print("EXISTE")
        df_stored = pd.read_csv("src/data/malwares.csv")
        df_result = pd.concat(
            [df_stored, df_recent], ignore_index=True
        ).drop_duplicates(subset=["SHA256"])
        df_result.to_csv("src/data/malwares.csv", index=False)
    return


if __name__ == "__main__":
    cluster()
