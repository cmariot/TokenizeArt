import requests
import os


def host_nft_image_on_ipfs(filename: str) -> str:


    # url = "https://uploads.pinata.cloud/v3/files"

    # payload = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"\r\n\r\n{}\r\n-----011000010111000001101001--\r\n\r\n"
    # headers = {
    #     "Authorization": "Bearer <token>",
    #     "Content-Type": "multipart/form-data"
    # }

    # response = requests.request("POST", url, data=payload, headers=headers)

    # print(response.text)

    url = "https://uploads.pinata.cloud/v3/files"
    headers = {
        'authorization': f'Bearer {os.environ.get("PINATA_JWT")}',
    }
    nft = open(filename, 'rb')

    # File to multipart form data

    response = requests.post(url, headers=headers, files={'file': nft})
    image_url = ""

    print(response.json())

    return image_url
