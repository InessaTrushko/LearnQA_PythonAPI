import requests


responce = requests.get("https://playground.learnqa.ru/api/long_redirect")

 #количество редиректов
countRedirect = len(responce.history)

first_responce = responce.history[0]
second_responce = responce

print(countRedirect)
print(first_responce.url)
print(second_responce.url)
