import requests

data = {'name': 'easy', 'age': 22}
r = requests.post('https://www.httpbin.org/post', data=data)
print(r.text)

r = requests.get('https://ssr1.scrape.center/')
print(type(r.status_code), r.status_code)
print(type(r.headers), r.headers)
print(type(r.cookies), r.cookies)
print(type(r.url), r.url)
print(type(r.history), r.history)

# request.codes
exit() if not r.status_code == requests.codes.ok else print('Request Successfully')

