

# from datetime import datetime, timedelta
# from zoneinfo import ZoneInfo
import asyncio

from bs4 import BeautifulSoup
import bs4.element
import requests
from fake_useragent import UserAgent

# from create_bot import bot, ID_CHANEL
# from data import orm
# from utils.parsers import UA

UA = UserAgent()


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



def pars_chita():
    url = 'https://www.chita.ru/text/'
    attr = {"class": "h9Jmx"}
    req_text = get_requests_text(url=url, params=UA.random)
    news = get_all_link(req_text, attr=attr, tag="h2")
    list_news = []
    for i in news:
        link_news = i.find("a").get("href")
        # print(link_news)
        # print(i.get_text())
        link_news = f'https://www.chita.ru{link_news}'
        list_news.append((i.get_text(), link_news))
    return list_news

def pars_zabnews():
    url = 'https://zabnews.ru/YandexRss.rss'
    req_text = get_requests_text(url=url, params=UA.random)
    soup = BeautifulSoup(req_text, 'xml')
    text = soup.find_all('item')
    list_news = []
    for i in text:
        link_news = i.find('link')
        text_news = i.find('title')
        list_news.append((text_news.text, link_news.text))
    return list_news[:21]
    # news = soup.get()
    # return(news)

    # attr = {"class": "h9Jmx"}
    #
    # news = get_all_link(req_text, attr=attr, tag="h2")
    # list_news = []
    # for i in news:
    #     link_news = i.find("a").get("href")
    #     # print(link_news)
    #     # print(i.get_text())
    #     link_news = f'https://www.chita.ru{link_news}'
    #     list_news.append((i.get_text(), link_news))
    # return list_news



s = pars_zabnews()

# a = pars_chita()
for i in s:
    print(i)