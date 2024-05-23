import re

# match 从头开始匹配
content = 'Hello 123 4567 World_This is a Regex Demo'
print(len(content))
result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}', content)
print(result)
print(result.group())
print(result.span())

# group ()提取分组
content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^Hello\s(\d+)\s\w{10}', content)
print(result)
print(result.group())
print(result.group(1))
print(result.span())

# 通用匹配
content = 'Hello 123 4567 World_This is a Regex Demo'
print(len(content))
result = re.match('^Hello.*Demo$', content)
print(result)
print(result.group())
print(result.span())

# 贪婪 非贪婪 匹配
content = 'Hello 123 4567 World_This is a Regex Demo'
print(len(content))
result = re.match('^He.*(\d+).*Demo$', content)
print(result)
print(result.group(1))
print(result.span())

result = re.match('^He.*?(\d+).*Demo$', content)

# 字符串中间用非贪婪 但结尾用非贪婪 可能匹配不到任何东西
content = 'http://weibo.com/comment/kEraCN'
result1 = re.match('http.*?comment/(.*)?', content)
result2 = re.match('http.*?comment/(.*)', content)
print(result1.group(1))
print(result2.group(1))

# re修饰符
content = '''Hello 1234567 World_This
 is a Regex Demo'''
result = re.match('^^He.*?(\d+).*?Demo$', content)
result = re.match('^^He.*?(\d+).*?Demo$', content, re.S)
print(result)
print(result.group())
print(result.group(1))
print(result.span())

# 转译 加\
content = '(百度)www.baidu.com'
result = re.match('\(百度\)www\.baidu\.com', content)
print(result)
