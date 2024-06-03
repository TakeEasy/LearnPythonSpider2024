import requests
import settings
import multiprocessing
from urllib import parse
from logging import config, getLogger
from os import makedirs
from os.path import exists
from pyquery import PyQuery as pq

config.dictConfig(settings.LOGGING_DIC)
logger_s = getLogger('console_print')

BASE_URL = 'https://www.javbus.com/star/wcd'
# BASE_URL = 'https://www.javbus.com'
# BASE_URL = 'https://www.baidu.com'
TOTAL_PAGE = 18
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'Upgrade-Insecure-Requests': '1',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6',
    'Cookie': 'existmag=all'
}
PROXIES = {
    'http': 'http://127.0.0.1:8627',
    'https': 'http://127.0.0.1:8627'
}

RESULTS_DIR = 'results'
exists(RESULTS_DIR) or makedirs(RESULTS_DIR)


def scrape_page(url):
    logger_s.info('scraping %s...', url)
    try:
        response = requests.get(url, headers=HEADERS, proxies=PROXIES)
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


if __name__ == '__main__':
    html = scrape_page(BASE_URL)
    # print(parse_index(html))
    for i, url in enumerate(parse_index(html)):
        print(i, url)
