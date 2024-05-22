import requests

s = requests.Session()
s.get('https://www.httpbin.org/cookies/set/number/12345678')
r = s.get('https://www.httpbin.org/cookies')
print(r.text)

# 忽略SSL错误
r = requests.get('https://ssr2.scrape.center/', verify=False)
print(r.text)

# 但是任然会有警报 可以忽略
from requests.packages import urllib3

urllib3.disable_warnings()

# 捕获日志 忽略
import logging

logging.captureWarnings(True)

# 设置本地证书
r = requests.get('https://ssr2.scrape.center/', cert=('/path/server.crt', '/path/server.key'))
