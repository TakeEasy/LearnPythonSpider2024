import httpx
import asyncio

response = httpx.get('https://www.httpbin.org/get')
print(response)
print(response.headers)
print(response.text)
print(response.status_code)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}
response = httpx.get('https://www.httpbin.org/get', headers=headers)
print(response.text)

# 默认还是用http1.1 需要开启http2
client = httpx.Client(http2=True)
response = client.get('https://spa16.scrape.center/')
print(response.text)

# 推荐用法
with httpx.Client(headers=headers, http2=True) as client:
    response = client.get('https://www.httpbin.org/get')
    print(response.text)
    print(response.http_version)  # 这个是requests库没有的哦

# 支持异步 async
url = 'https://www.httpbin.org/get'


async def fetch(url):
    async with httpx.AsyncClient(http2=True) as client:
        response = await client.get(url)
        print(response.text)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(fetch(url))
