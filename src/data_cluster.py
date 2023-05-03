import os
import pandas as pd
from data_cleaner import cleaner


def cluster():
    df1 = cleaner()
    # df2 = pd.read_csv("src/data/malwares.csv")
    if os.path.isfile(os.path.join("./data/", "malwares.csv")): 




# if __name__ == "__main__":
    # cluster()
