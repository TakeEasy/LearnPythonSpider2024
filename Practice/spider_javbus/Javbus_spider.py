import requests
import settings
import multiprocessing
import re
import pymongo
from urllib import parse
from logging import config, getLogger
from os import makedirs
from os.path import exists
from pyquery import PyQuery as pq

config.dictConfig(settings.LOGGING_DIC)
logger_s = getLogger('console_print')

BASE_URL = 'https://www.javbus.com/star/wcd'
ROOT_URL = 'https://www.javbus.com'
# BASE_URL = 'https://www.baidu.com'
TOTAL_PAGE = 1

MONGO_CONNECTION_STRING = 'mongodb://localhost:27017'
MONGO_DB_NAME = 'javbus'
MONGO_COLLECTION_NAME = 'avmovies'

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'Upgrade-Insecure-Requests': '1',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6',
    'cookie': 'existmag=all;'  # 不得劲 不好用 想带cookie还是用jar
}
jar = requests.cookies.RequestsCookieJar()
jar.set('existmag', 'all')
PROXIES = {
    'http': 'http://127.0.0.1:8627',
    'https': 'http://127.0.0.1:8627'
}

RESULTS_DIR = 'results'
exists(RESULTS_DIR) or makedirs(RESULTS_DIR)


def scrape_page(url):
    logger_s.info('scraping %s...', url)
    try:
        response = requests.get(url, headers=HEADERS, proxies=PROXIES, cookies=jar)
        if response.status_code == 200:
            return response.text
        logger_s.error('get invalid status code %s while scraping %s', response.status_code, url)
    except requests.RequestException:
        logger_s.error('error occurred while scraping %s', url, exc_info=True)


def scrape_index(page):
    index_url = f'{BASE_URL}/{page}'
    return scrape_page(index_url)


def parse_index(html):
    doc = pq(html)
    divs = doc('#waterfall:nth-child(2) div.item')
    # return divs
    # # detail_urls = []
    if not divs:
        return []
    for div in divs.items():
        detail_url = div('a').attr.href
        logger_s.info('get detail url %s', detail_url)
        yield detail_url


def scrape_detail(url):
    return scrape_page(url)


def parse_detail(html):
    doc = pq(html)
    info_div = doc('div.row.movie')

    image_url = parse.urljoin(ROOT_URL, info_div('div.screencap a').attr('href'))
    title = info_div.siblings('h3').text()
    code = info_div('div.info p:nth-child(1) span:nth-child(2)').text()

    info_div('div.info p:nth-child(2)').find('span').remove()
    publish_date = info_div('div.info p:nth-child(2)').text()

    info_div('div.info p:nth-child(3)').find('span').remove()
    how_long = re.search('(\d+)', info_div('div.info p:nth-child(3)').text()).group(1)

    director = ''
    if info_div('div.info p:nth-child(4)').find('span').text() == '導演:':
        director = info_div('div.info p:nth-child(4) a').text()

    productor = info_div('div.info p:nth-last-child(7) a').text()

    publisher = info_div('div.info p:nth-last-child(6) a').text()

    movie_classes_a = info_div('div.info p:nth-last-child(4) a')
    movie_classes = [a.text() for a in movie_classes_a.items()]

    star_a = info_div('div.info ul div.star-name a')
    actor_name = [a.text() for a in star_a.items()]

    if '合集' in movie_classes:
        return {}
    return {
        'code': code,
        'title': title,
        'image': image_url,
        'actor': actor_name,
        'publish_date': publish_date,
        'movielong': how_long,
        'director': director,
        'productor': productor,
        'publisher': publisher,
        'classes': movie_classes
    }


client = pymongo.MongoClient(MONGO_CONNECTION_STRING)
db = client[MONGO_DB_NAME]
collection = db[MONGO_COLLECTION_NAME]


def save_data(data):
    collection.update_one({
        'name': data.get('code')
    }, {
        '$set': data
    }, upsert=True)


def main():
    for page in range(1, TOTAL_PAGE + 1):
        index_html = scrape_index(page)
        for i, url in enumerate(parse_index(index_html)):
            detail_html = scrape_detail(url)
            movie_info = parse_detail(detail_html)
            if movie_info:
                save_data(movie_info)
                logger_s.info(f'movie: {movie_info.get("code")} save successfully')
            else:
                logger_s.info('旧电影合集 不予爬取')


if __name__ == '__main__':
    # html = scrape_page(BASE_URL)
    # # print(parse_index(html))
    # for i, url in enumerate(parse_index(html)):
    #     print(i, url)
    main()
