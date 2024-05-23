import re

content = 'Extra strings Hello 1234567 World_This is a Regex Demo dASD'
result = re.search('He.*?(\d+).*?Demo', content)
print(result)

# findall 找全部

# sub
content = '52a324a6basd5321adv'
content = re.sub('\d+', '', content)
print(content)

# compile 对正则表达式 多一层封装
content1 = '2019-12-21 12:00'
content2 = '2019-12-22 13:33'
content3 = '2019-12-23 15:66'
pattern = re.compile('\d{2}:\d{2}')
result1 = re.sub(pattern, '', content1)
result2 = re.sub(pattern, '', content2)
result3 = re.sub(pattern, '', content3)
print(result1, result2, result3)
