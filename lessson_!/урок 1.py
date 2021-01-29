import requests
import json
url = "https://www.google.ru"

respons = requests.get(url)
print(respons.status_code)
print(respons.headers)
print(respons.headers.get('Content-Type'))
print(respons.text) #основной запрос для работы тексктовое содержимое тела ответа от сервера
print("content")
print(respons.content) #отличается от респонс текст
print(respons.url)


# e5e4cd692a72b0b66ea0a6b80255d1c3
# api.openweathermap.org/data/2.5/weather?q={city name}&appid=e5e4cd692a72b0b66ea0a6b80255d1c3





access_token = "4a78288636beddb781b2451514853b4bcce8c7a6a4a685c8bf29fa389d86f00d9"

url = f"https://api.vk.com/method/groups.get?&count=10&v=5.51&access_token={access_token}"
response = requests.post(url)
#

print(response.text)
#print(j_data)

#print(f"В городе {j_data.get('name')} температура {j_data.get('main').get('temp') - 273.15} градусов")

asd = "https://api.github.com/users/subosito/repos"
ffff = requests.get(asd)
j_data = ffff.json()
#print(ffff.content)
print(j_data)
with open("new_file.json", "w+", encoding="utf-8") as file:
    json.dump(j_data, file, sort_keys=True)
