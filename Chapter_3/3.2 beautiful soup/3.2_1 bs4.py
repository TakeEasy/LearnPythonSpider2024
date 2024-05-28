import re

from bs4 import BeautifulSoup

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

# 选择解析库 创造的时候就已经补全标签了
soup = BeautifulSoup(html, 'lxml')
print(soup.prettify())
print(soup.title.string)

# 节点选择器  如果直接用节点名称 只能是第一个

print(soup.title)
print(type(soup.title))
print(soup.title.string)
print(soup.head)
print(soup.p)

# 提取属性
print(soup.title.name)

print(soup.p.attrs)
print(soup.p.attrs['name'])

print(soup.p['name'])
print(soup.p['class'])

print(soup.p.string)

# 嵌套选择
print(soup.head.title)
print(type(soup.head.title))
print(soup.head.title.string)

# 关联选择
print(soup.p.contens)  # 直接子节点 包括文本内容
print(soup.p.children)  # 同上 只不过返回的是生成器
for i, child in enumerate(soup.p.children):
    print(i, child)

print(soup.p.descendants)  # 所有子孙节点 生成器
for i, child in enumerate(soup.p.descendants):
    print(i, child)

print(soup.a.parent)  # 父节点

print(soup.p.parents)  # 祖先节点
print(list(enumerate(soup.a.parents)))

# 兄弟节点

print(soup.a.next_sibling)
print(soup.a.previous_sibling)
print(list(enumerate(soup.a.next_siblings)))
print(list(enumerate(soup.a.previous_siblings)))

# 提取信息
print(soup.a.next_sibling.string)
print(soup.a.previous_siblings[0].attrs['class'])

# 方法选择器

print(soup.find_all(name='ul'))
print(type(soup.find_all(name='ul')[0]))

for ul in soup.find_all(name='ul'):
    print(ul.find_all(name='li'))
    for li in ul.find_all(name='li'):
        print(li.string)

print(soup.find_all(attrs={'id': 'list-1'}))
print(soup.find_all(attrs={'name': 'elements'}))

print(soup.find_add(id='list-1'))
print(soup.find_add(class_='element'))  # class 是python里的关键字 所以后面加_

print(soup.find_all(text=re.compile('link')))  # text匹配节点内文本 可以是字符串 也可以是正则表达式

print(soup.find(name='ul'))  # find只会返回第一个

# find还有好多 find_parents find_parent find_next_siblings find_next_sibling...find_next


# CSS选择器
print(soup.select('.panel .panel-heading'))
print(soup.select('ul li'))
print(soup.select('#list-2 .element'))
print(type(soup.select('ul')[0]))
for ul in soup.select('ul'):
    print(ul.select('li'))
    print(ul['id'])
    print(ul.attrs['id'])

# 除了.string 还有.get_text()也可以获取节点内文本

for li in soup.select('li'):
    print(li.string)
    print(li.get_text())
