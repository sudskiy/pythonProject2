import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
from pprint import pprint   # красивее выводит сложные структуры


url = 'https://www.kinopoisk.ru'
my_params = {'quick_filters':'serials',
          'tab':'all'}

my_headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
           'Accept': '*/*'}

response = requests.get(url + '/popular/films/', params=my_params, headers = my_headers)

soup = bs(response.text, "html.parser")

# pprint(soup)
serials_block = soup.find('div',{'class':'selection-list'})
serials_list = serials_block.find_all('div',{'class':'desktop-rating-selection-film-item'})

# print(len(serials_list))
serials = []
for serial in serials_list:
    serial_data = {}
    serial_info = serial.find('p')
    serial_link = url + serial_info.parent['href']
    serial_name = serial_info.text
    serial_genre = serial.find('span',{'class':'selection-film-item-meta__meta-additional-item'})\
                         .next_sibling.text

    serial_rating = serial.find('span',{'class':'rating__value'}).text
    try:
        serial_rating = float(serial_rating)
    except:
        serial_rating = 0.0

    serial_data['name'] = serial_name
    serial_data['link'] = serial_link
    serial_data['genre'] = serial_genre
    serial_data['rating'] = serial_rating
    serials.append(serial_data)

pprint(serials)
