import requests
from bs4 import BeautifulSoup as bs
from pprint import pprint   # красивее выводит сложные структуры


url = 'http://...'
response = requests.get(url)

soup = bs(response.text, 'html.parser')
a = soup.find('a') #ищет до первого вхождения
b = soup.find_all('a') # все вхождения списком

parent_a  = a.parent # можно подниматься вверх до докуцмента(корня) через .parent.parent

parents_a = a.parents #возвращает всех родителей, но это никому не надо

div = soup.find('div')
children_div = div.children()  # ищет не только детей, а всех потомков
children_div = div.children(recursive=False)  # возвращает только детей

tags = soup.find_all(attrs={'href':"http://www.mail.ru"})


