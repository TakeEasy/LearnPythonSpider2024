import requests
import re

# r = requests.get('http://www.baidu.com')
# print(type(r))
# print(r.status_code)
# print(type(r.text))
# print(r.cookies)
#
# r.get('https://www.httpbin.org/get')
# r.post('https://www.httpbin.org/post')
# r.put('https://www.httpbin.org/put')
# r.delete('https://www.httpbin.org/delete')
# r.patch('https://www.httpbin.org/patch')

# get
# data = {
#     'name': 'easy',
#     'age': 22
# }
# r = requests.get('https://www.httpbin.org/get', params=data)
# print(r.text)
# print(r.json())
# print(type(r.json()))

# 抓取网页
r = requests.get('https://ssr1.scrape.center/')
pattern = re.compile('<h2.*?>(.*?)</h2>', re.S)
titles = re.findall(pattern, r.text)
print(titles)

# 抓取二进制文件
r = requests.get('https://scrape.center/favicon.ico')
print(r.text)
print(r.content)
with open('favicon.ico', 'wb') as f:
    f.write(r.content)

# 添加请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}
r = requests.get('https://ssr1.scrape.center/', headers=headers)
print(r.text)
