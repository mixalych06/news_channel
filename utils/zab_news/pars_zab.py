
# from datetime import datetime, timedelta
# from zoneinfo import ZoneInfo
import asyncio

from bs4 import BeautifulSoup
import bs4.element
import requests
from fake_useragent import UserAgent

# from create_bot import bot, ID_CHANEL
# from data import orm
from utils.parsers import UA, get_requests_text, get_all_link


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
    news = get_all_link(req_text, tag='item', features='xml')
    list_news = []
    for i in news:
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
def pars_zab():
    url = 'https://zab.ru/rss/'
    req_text = get_requests_text(url=url, params=UA.random)
    news = get_all_link(req_text, tag='item', features='xml')
    # soup = BeautifulSoup(req_text, 'xml')
    # text = soup.find_all('item')
    list_news = []
    for i in news:
        link_news = i.find('link')
        text_news = i.find('title')
        list_news.append((text_news.text, link_news.text))
    return list_news[:21]

def chita_pars():
    print('pars_chita')
    c=pars_chita()
    for i in c:
        print(i)
    print('pars_chita')
    b = pars_chita()
    for i in b:
        print(i)
    print('pars_chita')
    n = pars_chita()
    for i in n:
        print(i)
# async def sends_news(wait_for):
#     while True:
#         await asyncio.sleep(wait_for)
#         # await send_news_amurlife()
#         # await send_news_amurinfo()
#         # await send_news_asn24()
#         task2 = asyncio.create_task(send_news_amurlife())
#         task3 = asyncio.create_task(send_news_amurinfo())
#         task4 = asyncio.create_task(send_news_asn24())
