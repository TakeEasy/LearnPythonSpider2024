from urllib.request import Request, HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, ProxyHandler, build_opener
from urllib.error import URLError

username = 'admin'
password = 'admin'
url = 'https://ssr3.scrape.center/'

# 基础HTTP验证 handler
# p = HTTPPasswordMgrWithDefaultRealm()
# p.add_password(None, url, username, password)
# auth_handler = HTTPBasicAuthHandler(p)
# opener = build_opener(auth_handler)
#
# try:
#     result = opener.open(url)
#     html = result.read().decode('utf-8')
#     print(html)
# except URLError as e:
#     print(e.reason)

# proxy handler
proxy_handler = ProxyHandler({
    'http': 'http://127.0.0.1:8627',
    'https': 'https://127.0.0.1:8627'
})
opener = build_opener(proxy_handler)
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Accept-encoding': 'identify'  # 加这个头 否则有可能返回 压缩格式文件 无法直接读取
}
try:
    req = Request(url='https://www.python.org', headers=headers)
    response = opener.open(req)
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)

