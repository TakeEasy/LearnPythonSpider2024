import socket
import urllib.request
import urllib.parse
import urllib.error

# urllib.request.urlopen
# response = urllib.request.urlopen('http://www.baidu.com')
# response = urllib.request.urlopen('https://www.python.org')
# print(response.read().decode('utf-8'))
# print(response.status)
# print(response.getheaders())
# print(response.getheader('Server'))

# post urllib.parse.urlencode
# data = bytes(urllib.parse.urlencode({'name': 'easy'}), encoding='utf-8')
# print(urllib.parse.urlencode({'name': 'easy'}))
# response = urllib.request.urlopen('https://www.httpbin.org/post', data=data)
# print(response.read().decode('utf-8'))

# timeout urllib.error
# try:
#     response = urllib.request.urlopen('https://www.httpbin.org/get', timeout=0.1)
#     print(response.read().decode('utf-8'))
# except urllib.error.URLError as e:
#     if isinstance(e.reason, socket.timeout):
#         print('TIME OUT')

# urllib.request class
url = 'https://www.httpbin.org/post'
# url = 'https://www.python.org'
# url = 'https://www.baidu.com'
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    # 'Host': 'www.httpbin.org',
    'Accept-encoding': 'identify'  # 加这个头 否则有可能返回 压缩格式文件 无法直接读取
}
dict = {'name': 'easy'}
data = bytes(urllib.parse.urlencode(dict), encoding='utf-8')
req = urllib.request.Request(url=url, data=data, headers=headers, method='POST')
# req.add_header('Host', 'www.httpbin.org')
# req = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(req)
print(response.read().decode('utf-8'))
