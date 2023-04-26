import os
import requests
import pandas as pd
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())


def recent_malware():
    url = "https://mb-api.abuse.ch/api/v1/"
    headers = {"API-KEY": os.environ["API_KEY"]}
    data = {"query": "get_recent", "selector": "100"}
    malware_data = list()

    malwares = requests.post(
        url, data=data, timeout=15, headers=headers, allow_redirects=True
    ).json()

    for malware in malwares["data"]:
        malware_sha = malware["sha256_hash"]
        data_sha = {"query": "get_info", "hash": malware_sha}
        response_sha = requests.post(
            url, data=data_sha, timeout=15,
            headers=headers, allow_redirects=True
        )
        if response_sha.json()["query_status"] == "hash_not_found":
            print(">>>>>>  The sample hash was not found on Malbazaar <<<<<<")
        else:
            response_json = response_sha.json()
            df = pd.DataFrame(response_json["data"])
            df = df[
                [
                    "sha256_hash",
                    "signature",
                    "file_type",
                    "file_size",
                    "delivery_method",
                    "origin_country",
                    "first_seen",
                    "yara_rules",
                    "vendor_intel",
                ]
            ]
            malware_data.append(df.values.tolist()[0])
    table_headers = [
        "SHA256",
        "Familia",
        "Tipo Archivo",
        "cantidad",
        "Metodo de Entrega",
        "Origen",
        "Fecha",
        "REGLAS YARA",
        "INFORMES EXTERNOS",
    ]

    df = pd.DataFrame(malware_data, columns=table_headers)
    df.to_csv('./example.csv')
    return df


if __name__ == '__main__':
    recent_malware()
