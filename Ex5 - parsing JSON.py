import json

text_for_parsing = '{"messages": [{"message": "This is the first message","timestamp": "2021-06-04 16:40:53"},{"message": "And this is a second message", "timestamp": "2021-06-04 16:41:01"}]}'

key = "messages"
keyItem = "message"

obj = json.loads(text_for_parsing)[key][1]

if keyItem in obj:
    print(obj[keyItem])
else:
    print(f"Ключа {keyItem} в JSON нет")