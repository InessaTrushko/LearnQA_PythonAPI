import requests
import json
import time

url = "https://playground.learnqa.ru/ajax/api/longtime_job"
response = requests.get(url)

# Достаем параметры из ответов.
token_value = json.loads(response.text).get("token")
token = {'token': token_value}

seconds_value = json.loads(response.text).get("seconds")
seconds = {'seconds': seconds_value}

# ----- Cоздаем задачу
print("Creation task!")

response2 = requests.get(url, params=token)
result_first = json.loads(response2.text).get('status')

if result_first != 'Job is NOT ready':
    print("Task's status is not correct")
else:
    print("Task's status is correct")
    print(response2.text)
    print()


# ----- Ждем время выполнения задачи
print("Please wait " + str(seconds_value) + " seconds...")
print()

time.sleep(seconds_value)

# ----- проверяем задачу ещё раз
print("Сhecking task again...")

response3 = requests.get(url, params=token)
result_second = json.loads(response3.text).get('status')

if result_second != 'Job is ready':
    print("Task's status is not correct")
else:
    print("Task's status is correct")
    print(response3.text)
    print()

