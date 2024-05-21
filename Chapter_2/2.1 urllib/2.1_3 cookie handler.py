import http.cookiejar, urllib.request

url = 'http://www.baidu.com'
# cookie = http.cookiejar.CookieJar()
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open(url)
# for item in cookie:
#     print('{}={}'.format(item.name,item.value))

# 保存为Mozilla格式
filename = 'cookie.txt'
# cookie = http.cookiejar.MozillaCookieJar(filename)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open(url)
# cookie.save(ignore_discard=True, ignore_expires=True)

# 保存成LWP格式
# cookie = http.cookiejar.LWPCookieJar(filename)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open(url)
# cookie.save(ignore_discard=True, ignore_expires=True)

# 从文件读取cookie 访问网站 格式要对的上
cookie = http.cookiejar.LWPCookieJar()
cookie.load('cookie.txt', ignore_expires=True, ignore_discard=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open(url)
print(response.read().decode('utf-8'))
