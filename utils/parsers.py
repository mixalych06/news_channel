import locale

import pprint
from datetime import datetime, timedelta

import bs4.element
import requests

from bs4 import BeautifulSoup

locale.setlocale(locale.LC_ALL, "")

def get_requests_text(url: str, params: dict = None) -> str:
     '''
     Делает GET запрос по переданому URL
     :param url: URL запрашиваемой страницы
     :param params: параметры GET запроса (пример {'page': 1})
     :return: Возвращает HTML страницы в формате str
     '''
     reqs = requests.get(url, params=params)
     return reqs.text


def get_all_link(html_text: str, tag: str='a', attr: dict=None) -> bs4.element.ResultSet:
     '''
     Преобразует HTML в формате str в объект BS4
     :param html_text: HTML в формате str
     :param tag: tag для поиска
     :param attr: атрибут тега для поиска (пример {"class": "news__title"})
     :return: найденые элементы BS4
     '''
     soup = BeautifulSoup(html_text, 'html.parser')
     news = soup.find_all(tag, attr)
     return news


def converts_str_to_datetime(str_date: str):
     '''
     Преобразует строку в datetime
     :param str_date: str (21 декабря, 16:27, сегодня, 16:27, вчера, 16:27)
     :return: datetime
     '''
     day = str_date.split()
     if 'сегодня' in day[0]:
          date_news = datetime.today().strftime('%m-%d-%y')
          date_news =f'{date_news} {day[1]}'
          return datetime.strptime(date_news, '%m-%d-%y %H:%M')

     elif 'вчера' in day[0]:
          date_news = (datetime.today() - timedelta(days=1)).strftime('%m-%d-%y')
          date_news = f'{date_news} {day[1]}'
          return datetime.strptime(date_news, '%m-%d-%y %H:%M')

     else:
          date_news = str_date.split()
          print(date_news)
          if len(date_news) > 3:
               date_news = ' '.join(date_news)
               print(date_news)
               return datetime.strptime(date_news, '%d %B %Y, %H:%M')
          date_news.insert(2, str(datetime.now().year))
          date_news = ' '.join(date_news)
          return datetime.strptime(date_news, '%d %B, %Y %H:%M')


def pars_amur_life():
     url = 'https://www.amur.life/news'
     attr = {"class": "news__content news__content_bordered news__content_fixed"}
     req_text = get_requests_text(url=url)
     news = get_all_link(req_text, attr=attr, tag="div")
     dict_news = {}
     for i in news:
          link_news = i.find("a", {"class": "news__title"})
          date_news = converts_str_to_datetime(i.find("div", {"class": "mr-auto"}).text)
          dict_news[date_news] = (link_news.get_text(), link_news.get("href"))
     return dict_news




news = pars_amur_life()
print(news)
for d, n in sorted(news.items()):
     print(d)
     print(n)




# print(soup.a["news__title"])
