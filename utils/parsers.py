import locale

# from datetime import datetime, timedelta
# from zoneinfo import ZoneInfo
import asyncio

from bs4 import BeautifulSoup
import bs4.element
import requests
from fake_useragent import UserAgent

from create_bot import bot, ID_CHANEL
from data import orm
from data.models_amur import News_ASN24, News_AmurLife, News_AmurInfo

locale.setlocale(locale.LC_ALL, "")

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


def get_all_link(html_text: str, tag: str ='a', attr: dict = None, features='html.parser') -> bs4.element.ResultSet:
    '''
     Преобразует HTML в формате str в объект BS4
     :param html_text: HTML в формате str
     :param tag: tag для поиска
     :param attr: атрибут тега для поиска (пример {"class": "news__title"})
     :param features:
     :return: найденые элементы BS4
     '''
    soup = BeautifulSoup(html_text, features)
    news = soup.find_all(tag, attr)
    return news


# def converts_str_to_datetime(str_date: str):
#      '''
#      Преобразует строку в datetime
#      :param str_date: str (21 декабря, 16:27, сегодня, 16:27, вчера, 16:27)
#      :return: datetime
#      '''
#      day = str_date.split()
#      if 'сегодня' in day[0].lower():
#           date_news = datetime.now(tz=ZoneInfo('Asia/Yakutsk')).strftime('%m-%d-%y')
#           date_news =f'{date_news} {day[1]}'
#           return datetime.strptime(date_news, '%m-%d-%y %H:%M')
#
#      elif 'вчера' in day[0].lower():
#           date_news = (datetime.now(tz=ZoneInfo('Asia/Yakutsk')) - timedelta(days=1)).strftime('%m-%d-%y')
#           date_news = f'{date_news} {day[1]}'
#           return datetime.strptime(date_news, '%m-%d-%y %H:%M')
#
#      else:
#           date_news = str_date.split()
#           if len(date_news) > 3:
#                date_news = ' '.join(date_news)
#                return datetime.strptime(date_news, '%d %B %Y, %H:%M')
#           date_news.insert(2, str(datetime.now(tz=ZoneInfo('Asia/Yakutsk')).year))
#           date_news = ' '.join(date_news)
#           return datetime.strptime(date_news, '%d %B, %Y %H:%M')


def pars_amur_life():
    url = 'https://www.amur.life/news'
    attr = {"class": "news__content news__content_bordered news__content_fixed"}
    req_text = get_requests_text(url=url, params=UA.random)
    news = get_all_link(req_text, attr=attr, tag="div")
    list_news = []
    for i in news:
        link_news = i.find("a", {"class": "news__title"})
        # date_news = converts_str_to_datetime(i.find("div", {"class": "mr-auto"}).text)
        list_news.append((link_news.get_text(), link_news.get("href")))
    return list_news


# pars_amur_life()
def pars_asn24():
    url = 'https://asn24.ru/news/'
    req_text = get_requests_text(url=url, params=UA.random)
    attr = {"class": "blog-card"}
    news = get_all_link(req_text, attr=attr, tag="div")
    list_news = []
    for i in news[:20]:
        link_news = i.find("a", {"class": "link-as-card"})
        title = i.find("div", {"class": "blog-card__title"})
        # date_news = i.find("span", {"class": "blog-card__info-value"})
        # date_news = converts_str_to_datetime(date_news.text)
        list_news.append((title.get_text(), 'https://asn24.ru' + link_news.get("href")))
    return list_news


# pars_asn24()

def pars_amurinfo():
    url = 'https://amur.info/category/vse-novosti/'
    req_text = get_requests_text(url=url, params=UA.random)
    attr = {"class": "long-news-block with-text"}
    news = get_all_link(req_text, attr=attr, tag="div")
    list_news = []
    for i in news:
        link_news = i.find("a", {"class": "h2"})
        title = i.find("a", {"class": "h2"})
        # date_news = i.find("a", {"class": "news-date"})
        # date_news = converts_str_to_datetime(date_news.text)
        list_news.append((title.get_text(), link_news.get("href")))
    return list_news


# pars_amurinfo()

async def check_add_news(news_dict, model):
    latest_news = await orm.get_max_date(model)
    if latest_news in news_dict:
        await orm.add_news(news_dict[:news_dict.index(latest_news)], latest_news, model)
    else:
        await orm.add_news(news_dict, latest_news, model)


async def start_checks_for_news_amur_life(wait_for):
    while True:
        await asyncio.sleep(wait_for)
        news_amur = pars_amur_life()
        await check_add_news(news_amur, News_AmurLife)


async def start_checks_for_news_asn24(wait_for):
    while True:
        await asyncio.sleep(wait_for)
        news_asn24 = pars_asn24()
        await check_add_news(news_asn24, News_ASN24)


async def start_checks_for_news_amurinfo(wait_for):
    while True:
        await asyncio.sleep(wait_for)
        news_amurinfo = pars_amurinfo()
        await check_add_news(news_amurinfo, News_AmurInfo)


async def send_news_asn24():
    news = await orm.get_min_date(News_ASN24)
    if news:
        await orm.update_completed(news.id, News_ASN24)
        await bot.send_message(chat_id=ID_CHANEL,
                               text=f'{news.link}')


async def send_news_amurlife():
    news2 = await orm.get_min_date(News_AmurLife)
    if news2:
        await orm.update_completed(news2.id, News_AmurLife)
        await bot.send_message(chat_id=ID_CHANEL,
                               text=f'{news2.link}')


async def send_news_amurinfo():
    news3 = await orm.get_min_date(News_AmurInfo)
    if news3:
        await orm.update_completed(news3.id, News_AmurInfo)
        await bot.send_message(chat_id=ID_CHANEL,
                               text=f'{news3.link}')


async def sends_news(wait_for):
    while True:
        await asyncio.sleep(wait_for)
        # await send_news_amurlife()
        # await send_news_amurinfo()
        # await send_news_asn24()
        task2 = asyncio.create_task(send_news_amurlife())
        task3 = asyncio.create_task(send_news_amurinfo())
        task4 = asyncio.create_task(send_news_asn24())

# asyncio.run(checks_for_news())
