import requests
from pyquery import PyQuery as pq
import re

URL = 'https://ssr1.scrape.center'
html = requests.get(URL).text
doc = pq(html)

items = doc('.el-card').items()

with open('movies.txt', 'w', encoding='utf-8') as f:
    for item in items:
        name = item.find('a > h2').text()
        f.write(f'name:{name}\n')
        categories = [item.text() for item in item.find('.categories button span').items()]
        f.write(f'categories:{categories}\n')
        published_at = item.find('.info:contains(上映)').text()
        published_at = re.search('(\d{4}-\d{2}-\d{2})', published_at).group(1) \
            if published_at and re.search('(\d{4}-\d{2}-\d{2})', published_at) else None
        f.write(f'published_at:{published_at}\n')
        score = item.find('p.score').text()
        f.write(f'score:{score}\n')
        f.write(f'{"=" * 50}\n')


