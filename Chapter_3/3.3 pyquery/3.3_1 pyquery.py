from pyquery import PyQuery as pq

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

doc = pq(html)
print(doc('li'))

# 可以直接传url
doc = pq(url='https://cuiqingcai.com')
print(doc('title'))

# 也可以从文件
doc = pq(filename='demo.html')
print(doc('li'))

# 基本css选择器
print(doc('#container .list li'))
print(type(doc('#container .list li')))

for item in doc('#container .list li').items():
    print(item.text())

# 查找节点
# 子节点
items = doc('.list')
print(type(items))
print(items)
lis = items.find('li')
print(type(items))
print(items)

lis = items.children()
print(lis)
lis = items.children('.active')
print(lis)

# 父节点
items = doc('.list')
container = items.parent()
print(container)
container = items.parents()
print(container)
parent = items.parents('.wrap')
print(parent)

# 兄弟节点
li = doc('.list .item-0.active')
print(li.siblings())
print(li.siblings('.active'))

# 遍历节点
lis = doc('li').items()
print(type(lis))
for li in lis:
    print(li, type(li))

# 获取信息
a = doc('.item-0.active a')
print(a, type(a))
print(a.attr('href'))
print(a.attr.href)

# 如果多个.attr 只能返回第一个节点的属性
a = doc('a')
print(a.attr.href)

for item in a.items():
    print(item.attr.href)

# 获取文本
a = doc('.item-0.active a')
print(a)
print(a.text())  # 只会返回纯文本
print(a.html())  # 返回html所有内容

# 节点操作
li = doc('.item-0.active')
print(li)
li.removeClass('active')
print(li)
li.addClass('active')
print(li)

li.attr('name','link')
print(li)
li.text('changed item')
print(li)
li.html('<span>changed item</span>')
print(li)

wrap = doc('.wrap')
print(wrap.text())
wrap.find('p').remove()
print(wrap.text())

# 伪类选择器
li = doc('li:first-child')
print(li)
li = doc('li:last-child')
print(li)
li = doc('li:nth-child(2)')
print(li)
li = doc('li:gt(2)')
print(li)
li = doc('li:nth-child(2n)')
print(li)
li = doc('li:contains(second)')
print(li)

