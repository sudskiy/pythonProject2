import requests

url = "https://www.google.ru"

respons = requests.get(url)
print(respons.status_code)
print(respons.headers)
print(respons.headers.get('Content-Type'))
print(respons.text) #основной запрос для работы тексктовое содержимое тела ответа от сервера
print("content")
print(respons.content) #отличается от респонс текст
print(respons.url)