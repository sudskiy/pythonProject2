from bs4 import BeautifulSoup as bs
import requests
from pprint import pprint
import re

"""
vacancy - название вакансии,
pages - количество страниц для поиска

"""

def hh(vacancy, pages):

    job_headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                                ' Chrome/88.0.4324.150 Safari/537.36', 'Accept': '*/*'}
    response = requests.get('https://hh.ru/search/vacancy?area=0&fromSearchLine=true&st=searchVacancy&text=' + vacancy,
                            headers=job_headers)
    soup = bs(response.text, 'html.parser')
    pg = 0

    jobs = []
    for list in range(pages):
        pg += 1
        job = soup.find('div', {'class': 'vacancy-serp'})
        vacancies = job.find_all('div', {'class': 'vacancy-serp-item'})
        for vacancy in vacancies:
            vacancy_data = {}
            vacancy_name = vacancy.find('span', {'class': 'g-user-content'}).getText()
            vacancy_company = vacancy.find('div', {'class': 'vacancy-serp-item__meta-info'}).find('a').getText()
            vacancy_url = vacancy.find('span', {'class': 'g-user-content'}).find('a')['href']
            location = vacancy.find('span', {'class': 'vacancy-serp-item__meta-info'})
            if not location:
                location = None
            else:
                location = location.getText()
            salary = vacancy.find('span', {'data-qa': 'vacancy-serp__vacancy-compensation'})
            if not salary:
                salary_min = None
                salary_max = None
                salary_currency = None
            else:
                salary = salary.getText().replace(u'\xa0', u'')
                salary = re.split(r'\s|-', salary)

                if salary[0] == 'до':
                    salary_min = None
                    salary_max = int(salary[1])
                elif salary[0] == 'от':
                    salary_min = int(salary[1])
                    salary_max = None
                else:
                    salary_min = int(salary[0])
                    salary_max = int(salary[1])

                salary_currency = salary[2]

            vacancy_data['salary_min'] = salary_min
            vacancy_data['salary_max'] = salary_max
            vacancy_data['salary_currency'] = salary_currency

            vacancy_data['job'] = vacancy_name
            vacancy_data['url'] = vacancy_url
            vacancy_data['company_name'] = vacancy_company
            vacancy_data['location'] = location
            jobs.append(vacancy_data)

        if not soup.find('a', {'class': 'bloko-button HH-Pager-Controls-Next HH-Pager-Control'}):
            break
        next_page = soup.find('a',{'class':'bloko-button HH-Pager-Controls-Next HH-Pager-Control'})
        next_page_link = next_page['href']
        resp = requests.get('https://hh.ru' + next_page_link, headers=job_headers)
        soup = bs(resp.text, 'html.parser')

    pprint(jobs)
    print("Результат выведен по ", pg, " страницам")
    return(jobs)


search = 'Python'
pages = 5

hh(search, pages)