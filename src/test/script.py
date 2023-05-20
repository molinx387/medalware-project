import pycountry
import pandas as pd

df = pd.read_csv("src/data/malwares.csv")

def convert_alpha2_to_alpha3(df):
    alpha2_to_alpha3 = {country.alpha_2: country.alpha_3 for country in pycountry.countries}
    df['Origen'] = df['Origen'].map(alpha2_to_alpha3)
convert_alpha2_to_alpha3(df)
df.to_csv("src/data/malwares.csv", index=False)


