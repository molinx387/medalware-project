import os
import requests
import pandas as pd
from dotenv import load_dotenv, find_dotenv
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
import pycountry
from pages.definition.malware_definitions import malware_dict

load_dotenv(find_dotenv())


def data_extractor():
    url = "https://mb-api.abuse.ch/api/v1/"
    headers = {"API-KEY": os.environ["API_KEY"]}
    data = {"query": "get_recent", "selector": "100"}
    malware_data = list()
    session = requests.Session()
    retries = Retry(total=5, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
    session.mount("https://", HTTPAdapter(max_retries=retries))
    malwares = requests.post(
        url, data=data, timeout=15, headers=headers, allow_redirects=True
    ).json()
    for malware in malwares["data"]:
        malware_sha = malware["sha256_hash"]
        data_sha = {"query": "get_info", "hash": malware_sha}
        response_sha = requests.post(
            url, data=data_sha, timeout=15, headers=headers, allow_redirects=True
        )
        if response_sha.json()["query_status"] == "hash_not_found":
            print(">>>>>>  The sample hash was not found on Malbazaar <<<<<<")
        else:
            response_json = response_sha.json()
            df = pd.DataFrame(response_json["data"])
            df = df[
                [
                    "first_seen",
                    "sha256_hash",
                    "signature",
                    "delivery_method",
                    "file_type",
                    "file_size",
                    "origin_country",
                ]
            ]
            malware_data.append(df.values.tolist()[0])
    table_headers = [
        "Fecha",
        "SHA256",
        "Malware",
        "Metodo de Entrega",
        "Extension",
        "Peso",
        "Origen",
    ]
    df = pd.DataFrame(malware_data, columns=table_headers)
    df.insert(3, "Familia", " ")
    df.insert(4, "SO", " ")

    for dictionary in malware_dict:
        # Check if the value of the key "Nombre" is in the Malware column of the dataframe
        mask = df["Malware"] == dictionary["Malware"]
        if mask.any():
            # Update the values in the "Familia" column where the condition is True
            df.loc[mask, "Familia"] = dictionary["Familia"]
            df.loc[mask, "SO"] = dictionary["SO"]
        else:
            df.loc[mask, "Familia"] = "Desconocida"
            df.loc[mask, "SO"] = "Desconocido"

    return df


def data_local(df):
    for dictionary in malware_dict:
        # Check if the value of the key "Nombre" is in the Malware column of the dataframe
        mask = df["Malware"] == dictionary["Malware"]
        if mask.any():
            # Update the values in the "Familia" column where the condition is True
            df.loc[mask, "Familia"] = dictionary["Familia"]
            df.loc[mask, "SO"] = dictionary["SO"]
        else:
            df.loc[mask, "Familia"] = "Desconocida"
            df.loc[mask, "SO"] = "Desconocido"

    return df


def data_cleaner(df):
    df["Fecha"] = pd.to_datetime(df["Fecha"])
    df["Metodo de Entrega"].fillna("Otros", inplace=True)
    df["Metodo de Entrega"] = df["Metodo de Entrega"].map(
        {
            "web_download": "Descarga web",
            "other": "Otro",
            "email_attachment": "Adjunto en email",
            "web_drive-by": "Descarga involuntaria",
            "email_link": "Link de email",
            "multiple": "multiple",
        }
    )
    df.dropna(inplace=True)
    alpha_country = {
        country.alpha_2: country.alpha_3 for country in pycountry.countries
    }
    df["Origen"] = df["Origen"].map(alpha_country)
    df.reset_index(drop=True, inplace=True)
    return df


def data_cluster(df):
    csv_path = "src/data/malwares.csv"
    df_recent = df
    if os.path.isfile(csv_path):
        df_stored = pd.read_csv(csv_path)
        df_result = pd.concat(
            [df_stored, df_recent], ignore_index=True
        ).drop_duplicates(subset=["SHA256"])
        df_updated = data_local(df_result)
        df_updated.to_csv(csv_path, index=False)
    else:
        df_stored = df_recent
        df_stored.to_csv(csv_path, index=False)


def data_updater():
    df = data_extractor()
    df = data_local(df)
    df = data_cleaner(df)
    df = data_cluster(df)


if __name__ == "__main__":
    data_updater()
