import requests
from requests.auth import HTTPBasicAuth

# timeout 可以分开 连接时间和读取时间
r = requests.get('https://www.httpbin.org/get', timeout=1)
r = requests.get('https://www.httpbin.org/get', timeout=(5, 30))

r = requests.get('https://ssr3.scrape.center/', auth=HTTPBasicAuth('admin', 'admin'))
print(r.status_code)

# 可以不用HTTPBasicAuth 直接传元组 默认就是用它
r = requests.get('https://ssr3.scrape.center/', auth=('admin', 'admin'))

# 安装 requests_oauthlib库 可以用 oauth验证

# 代理
proxies = {
    'http': 'http://127.0.0.1:8627',
    'https': 'https://127.0.0.1:8627'
}
r = requests.get('https://www.httpbin.org/get', proxies=proxies)
# 安装 "requests[socks]" 库 可以支持socks代理
