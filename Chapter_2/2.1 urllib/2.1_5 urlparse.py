from urllib.parse import urlparse, urlunparse, urlsplit, urlunsplit, urljoin, urlencode, parse_qs, parse_qsl, quote, \
    unquote

# urlparse
result = urlparse('https://www.baidu.com/index.html;user?id=5#comment')
print(type(result))
print(result)

result = urlparse('https://www.baidu.com/index.html;user?id=5#comment', scheme='http', allow_fragments=False)
print(result)

print(result.scheme, result[0], result.netloc, result[1], sep='\n')

# urlunparse
data = ['https', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
print(urlunparse(data))

# urlsplit urlunsplit 跟urlparse差不多 只不过 params 划到 path里
result = urlsplit('https://www.baidu.com/index.html;user?id=5#comment')
print(type(result))
print(result, result.scheme, result[0], sep='\n')

data = ['https', 'www.baidu.com', 'index.html', 'a=6', 'comment']
print(urlunparse(data))

# urljoin 拼url链接 用第一个参数的scheme,netloc,path 补充第二个参数url 缺失的部分
print(urljoin('https://www.baidu.com', 'FAQ.html'))
print(urljoin('https://www.baidu.com', 'https://www.cuiqingcai.com/FAQ.html'))
print(urljoin('https://www.baidu.com/about.html', 'https://www.cuiqingcai.com/FAQ.html'))
print(urljoin('https://www.baidu.com/about.html', 'https://www.cuiqingcai.com/FAQ.html'))
print(urljoin('https://www.baidu.com?wd=abc', 'https://www.cuiqingcai.com/index.php'))
print(urljoin('https://www.baidu.com', '?category=2#comment'))
print(urljoin('www.baidu.com', '?category=2#comment'))
print(urljoin('https://www.baidu.com#comment', '?category=2'))

# urlencode 字典转url参数 parse_qs 反过来 parse_qsl 反过来元组
params = {
    'name': 'easy',
    'age': 20
}
base_url = 'https://www.baidu.com?'
url = base_url + urlencode(params)
print(url)

query = 'name=easy&age=20'
print(parse_qs(query))
print(parse_qsl(query))

# quote, unquote 将内容转成url编码格式 反过来
keyword = '赤壁'
url = 'https://www.baidu.com/s?wd=' + quote(keyword)
print(url)
print(unquote(url))


