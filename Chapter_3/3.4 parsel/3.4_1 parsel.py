from parsel import Selector

html = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dormouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
<a href="http://example.com/tillie" class="sister" id="link3">Tillie   </a>
and they lived at the bottom of a well.</p>
<p class="story">...</p>
'''

selector = Selector(text=html)

# 既可以用xpath 也可以用cssselector
items = selector.css('.item-0')
print(len(items), type(items), items)
items = selector.xpath('//li[contains(@class,"item-0")]')
print(len(items), type(items), items)

# 提取文本
items = selector.css('.item-0')
for item in items:
    text = item.xpath('.//text()').get()
    print(text)

result = selector.xpath('//li[contains(@class,"item-0")]//text()').get()
print(result)
result = selector.xpath('//li[contains(@class,"item-0")]//text()').getall()
print(result)

# 提取属性
result = selector.css('.item-0.active a::attr(href)').get()
print(result)
resutl = selector.xpath('//li[contains(@class,"item-0") and contains(@class,"active")]/a/@href').get()
print(result)

# 正则提取
result = selector.css('.item-0').re('link.*')
print(resutl)

result = selector.css('.item-0 *::text').re('.*item')
print(result)

result = selector.css('.item-0').re_first('<span class="bold">(.*?)</span>')

