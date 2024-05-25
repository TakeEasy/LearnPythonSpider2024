import requests
import re
import settings
import json
import multiprocessing
from urllib.parse import urljoin
from logging import config, getLogger
from os import makedirs
from os.path import exists

config.dictConfig(settings.LOGGING_DIC)
logger_s = getLogger('console_print')

BASE_URL = 'https://ssr1.scrape.center'
TOTAL_PAGE = 10

RESULTS_DIR = 'results'
exists(RESULTS_DIR) or makedirs(RESULTS_DIR)


def save_data(data):
    try:
        name = data.get('name').replace(':', '-')
        data_path = f'{RESULTS_DIR}/{name}.json'
        json.dump(data, open(data_path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    except Exception as e:
        logger_s.error('error occurred while saving %s', data.get('name'), exc_info=True)


def scrape_page(url):
    logger_s.info('scraping %s...', url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        logger_s.error('get invalid status code %s while scraping %s', response.status_code, url)
    except requests.RequestException:
        logger_s.error('error occurred while scraping %s', url, exc_info=True)


def scrape_index(page):
    index_url = f'{BASE_URL}/page/{page}'
    return scrape_page(index_url)


def parse_index(html):
    pattern = re.compile('<a.*?href="(.*?)".*?class="name">')
    items = re.findall(pattern, html)
    if not items:
        return []
    for item in items:
        detail_url = urljoin(BASE_URL, item)
        logger_s.info('get detail url %s', detail_url)
        yield detail_url


def scrape_detail(url):
    return scrape_page(url)


def parse_detail(html):
    cover_pattern = re.compile('class="item.*?<img.*?src="(.*?)".*?class="cover">', re.S)
    name_pattern = re.compile('<h2.*?>(.*?)</h2>')
    categories_pattern = re.compile('<button.*?category.*?<span>(.*?)</span>.*?</button>', re.S)
    published_at_pattern = re.compile('(\d{4}-\d{2}-\d{2}\s?上映)', re.S)
    drama_pattern = re.compile('<div.*?drama.*?>.*?<p.*?>(.*?)</p>', re.S)
    score_pattern = re.compile('<p.*?score.*?>(.*?)</p>', re.S)
    cover = re.search(cover_pattern, html).group(1).strip() if re.search(cover_pattern, html) else None
    name = re.search(name_pattern, html).group(1).strip() if re.search(name_pattern, html) else None
    categories = re.findall(categories_pattern, html) if re.findall(categories_pattern, html) else []
    published_at = re.search(published_at_pattern, html).group(1).strip() if re.search(published_at_pattern,
                                                                                       html) else None
    drama = re.search(drama_pattern, html).group(1).strip() if re.search(drama_pattern, html) else None
    score = re.search(score_pattern, html).group(1).strip() if re.search(score_pattern, html) else None

    return {
        'cover': cover,
        'name': name,
        'categories': categories,
        'published_at': published_at,
        'drama': drama,
        'score': score
    }


def main():
    for page in range(1, TOTAL_PAGE + 1):
        index_html = scrape_index(page)
        detail_urls = parse_index(index_html)
        for detail_url in detail_urls:
            detail_html = scrape_detail(detail_url)
            data = parse_detail(detail_html)
            logger_s.info('get detail data %s', data)
            logger_s.info('saving data to json file')
            save_data(data)
            logger_s.info('data saved successfully')
        # logger_s.info('detail urls %s', list(detail_urls))


def main_multiprocess(page):
    index_html = scrape_index(page)
    detail_urls = parse_index(index_html)
    for detail_url in detail_urls:
        detail_html = scrape_detail(detail_url)
        data = parse_detail(detail_html)
        logger_s.info('get detail data %s', data)
        logger_s.info('saving data to json file')
        save_data(data)
        logger_s.info('data saved successfully')


if __name__ == '__main__':
    # main()

    # html = scrape_detail('https://ssr1.scrape.center/detail/16')
    # data = parse_detail(html)
    # print(data)
    # save_data(data)

    pool = multiprocessing.Pool()
    pages = range(1, TOTAL_PAGE + 1)
    pool.map(main_multiprocess, pages)
    pool.close()
    pool.join()
