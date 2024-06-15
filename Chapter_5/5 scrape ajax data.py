import requests
import settings
import pymongo
from logging import config, getLogger

BASE_URL = 'https://spa1.scrape.center/'
AJAX_URL = 'https://spa1.scrape.center/api/movie/?limit={limit}&offset={offset}'
LIMIT = 10
DETAIL_URL = 'https://spa1.scrape.center/api/movie/{id}'
TOTAL_PAGES = 1

# mongodb connection
MONGO_CONNECTION_STRING = 'mongodb://localhost:27017'
MONGO_DB_NAME = 'javbus'
MONGO_COLLECTION_NAME = 'movies'

# html = requests.get(BASE_URL).text
# print(html)

config.dictConfig(settings.LOGGING_DIC)
logger_s = getLogger('console_print')


def scrape_api(url):
    logger_s.info('scraping %s...', url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        logger_s.error('get invalid status code %s while scraping %s', response.status_code, url)
    except requests.RequestException:
        logger_s.error('error occurred while scraping %s', url, exc_info=True)


def scrape_index(page):
    url = AJAX_URL.format(limit=LIMIT, offset=LIMIT * (page - 1))
    return scrape_api(url)


def scrape_detail(id):
    url = DETAIL_URL.format(id=id)
    return scrape_api(url)


client = pymongo.MongoClient(MONGO_CONNECTION_STRING)
db = client[MONGO_DB_NAME]
collection = db[MONGO_COLLECTION_NAME]


def save_data(data):
    collection.update_one({
        'name': data.get('name')
    }, {
        '$set': data
    }, upsert=True)


def main():
    for page in range(1, TOTAL_PAGES + 1):
        index_data = scrape_index(page)
        for item in index_data.get('results'):
            id = item.get('id')
            detail_data = scrape_detail(id)
            logger_s.info('detail data %s', detail_data)
            save_data(detail_data)
            logger_s.info('data saved successfully')


if __name__ == '__main__':
    main()
    # logger_s.info('hahaha')
