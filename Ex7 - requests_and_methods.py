import requests
import json

# Для запуска выполнения пункта задания, выбрать необходимый task_point:  point_1, point_2, point_3, point_4
# Для запуска всех пунктов, указать task_point = "all"
task = 7
task_point = "all"


if task_point == "point_1" or (task == 7 and task_point == "all"):
        print("Point_1: ")

        # Point_1
        # Делает http-запрос любого типа без параметра method, описать что будет выводиться в этом случае
        responce_1_1 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
        responce_1_2 = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type")
        responce_1_3 = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type")
        responce_1_4 = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type")

        print(" Method_GET: ", responce_1_1.text)
        print(" Method_POST: ", responce_1_2.text)
        print(" Method_PUT: ", responce_1_3.text)
        print(" Method_DELETE: ", responce_1_4.text)

        # ОТВЕТ: внутри метода  возможно реализована обработка ошибок. Если не правильный метод используется (без параметров),
        # обработчик будет выводить адекватную ошибку ввиде текста с объяснение. Так как для данного метода необходим параметр.
        # Если мы не передали параметр, запрос не смог выполниться и вывести необходимые для нас данные.


if task_point == "point_2" or (task == 7 and task_point == "all"):
        print()
        print("Point_2: ")

        # Point_2
        # Делает http-запрос не из списка. Например, HEAD. Описать что будет выводиться в этом случае.

        responce_2_1 = requests.patch("https://playground.learnqa.ru/ajax/api/compare_query_type")
        responce_2_2 = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type")

        print(" Method_PATCH: ", responce_2_1.text)
        print(" Method_HEAD: ", responce_2_2.text)


        # ОТВЕТ:Метод HEAD, возвращает заголовки запросов. Во втором случае, заголовок запроса пустой,
        # а значит все необходимые для нас данные лежат в теле запроса. Поэтому, все методы из пункта 1 возвращают ошибку.
        # Так как метод GET не имеет тела запроса, все параметры метода передаются в самом урле.

if task_point == "point_3" or (task == 7 and task_point == "all"):
        print()
        print("Point_3: ")

        # Point_3
        # 3. Делает запрос с правильным значением method. Описать что будет выводиться в этом случае.

        payload = {"method":"GET"}
        data_2 = {"method":"POST"}
        data_3 = {"method":"PUT"}
        data_4 = {"method":"DELETE"}

        responce_3_1 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type",params=payload)
        responce_3_2 = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=data_2)
        responce_3_3 = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data=data_3)
        responce_3_4 = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data=data_4)

        print(responce_3_1.text)
        print(responce_3_2.text)
        print(responce_3_3.text)
        print(responce_3_4.text)

if task_point == "point_4" or (task == 7 and task_point == "all"):
        print()
        print("Point_4: ")

        # Point_4
        # С помощью цикла проверяет все возможные сочетания реальных типов запроса и значений параметра method.
        # Например с GET-запросом передает значения параметра method равное ‘GET’, затем ‘POST’, ‘PUT’, ‘DELETE’ и так далее.
        # И так для всех типов запроса. Найти такое сочетание, когда реальный тип запроса не совпадает со значением параметра,
        # но сервер отвечает так, словно все ок. Или же наоборот, когда типы совпадают, но сервер считает, что это не так.

        methods = ["POST", "GET", "PUT", "DELETE"]
        req = ["POST", "GET", "PUT", "DELETE"]
        url = "https://playground.learnqa.ru/ajax/api/compare_query_type"

        for i in req:
                for j in methods:
                        result = i +"_" + j

                        getParams = {"method": j}
                        if i == "GET":
                                response  = requests.get(url, params=getParams)
                                if response.text.__contains__("success"):
                                        print(result + ": " + response.text)
                        if i == "POST":
                                response = requests.post(url, data=getParams)
                                if response.text.__contains__("success"):
                                        print(result + ": " + response.text)
                        if i == "PUT":
                                response = requests.put(url, data=getParams)
                                if response.text.__contains__("success"):
                                        print(result + ": " + response.text)
                        if i == "DELETE":
                                response = requests.delete(url, data=getParams)
                                if response.text.__contains__("success"):
                                        print(result + ": " + response.text)


