import requests

# r = requests.get('http://www.baidu.com')
# print(r.cookies)
# for key, value in r.cookies.items():
#     print('{}={}'.format(key, value))
#
# headers = {
#     'Cookie': '_device_id=27efac4be4f729468601b4693c3d006d; _octo=GH1.1.859514837.1709388416; saved_user_sessions=13162283%3AlHQ9ab2KjVEDSpc-zop3da3bDDFIznovOnjenBGfAH-K7yj2; user_session=lHQ9ab2KjVEDSpc-zop3da3bDDFIznovOnjenBGfAH-K7yj2; __Host-user_session_same_site=lHQ9ab2KjVEDSpc-zop3da3bDDFIznovOnjenBGfAH-K7yj2; logged_in=yes; dotcom_user=TakeEasy; has_recent_activity=1; color_mode=%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D; preferred_color_mode=light; tz=Asia%2FShanghai; _gh_sess=TA8zKpS7iY%2B%2BGvQ0cO1g%2B08SUmGGBTbZsq%2FR1bEcpho0dnwcWo43QORKOlcP%2BmLJ65THVP8jmmA%2FsEL62ieJSYLuXZ0xO%2FnJy0sDALFSoGLoT2IZqy0DMGS1QkmhQHpa%2Fj6K5N%2BNvp02kf%2B%2FAUcQw9oSORQv%2Fx7ItlcTVrTVGq3E2vsvjlNPp%2FKsE5T3WG4O%2F7X43w%2BMKbYwz7QQoE9AZMdkCc%2BXabxrE%2FSn6mHKWoAj1F5hKPcOFKIkGds3zuBDm1ILyQkMMtL3IL5mD4fKRW5jq7t8RU669aHmNuYL%2FMBye8%2FzAHK2c5SHNGt7kncrdqiOVqJfNFHyfhbap4tsCh7gmnZjPTGzgx8EM%2B6Qo71TrI%2BTODNEwGNuyyAQcNkx--lqAIWltrlbnvu3Xb--bl4RgDDag3fM0ntF6DWQrw%3D%3D'
# }
# r = requests.get('https://www.github.com/', headers=headers)
# print(r.text)

# 通过RequestsCookieJar设置Cookie
cookies = "_device_id=27efac4be4f729468601b4693c3d006d; _octo=GH1.1.859514837.1709388416; " \
          "saved_user_sessions=13162283%3AlHQ9ab2KjVEDSpc-zop3da3bDDFIznovOnjenBGfAH-K7yj2; " \
          "user_session=lHQ9ab2KjVEDSpc-zop3da3bDDFIznovOnjenBGfAH-K7yj2; " \
          "__Host-user_session_same_site=lHQ9ab2KjVEDSpc-zop3da3bDDFIznovOnjenBGfAH-K7yj2; logged_in=yes; " \
          "dotcom_user=TakeEasy; has_recent_activity=1; " \
          "color_mode=%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C" \
          "%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A" \
          "%22dark%22%7D%7D; preferred_color_mode=light; tz=Asia%2FShanghai; " \
          "_gh_sess=TA8zKpS7iY%2B%2BGvQ0cO1g%2B08SUmGGBTbZsq%2FR1bEcpho0dnwcWo43QORKOlcP%2BmLJ65THVP8jmmA" \
          "%2FsEL62ieJSYLuXZ0xO%2FnJy0sDALFSoGLoT2IZqy0DMGS1QkmhQHpa%2Fj6K5N%2BNvp02kf%2B%2FAUcQw9oSORQv" \
          "%2Fx7ItlcTVrTVGq3E2vsvjlNPp%2FKsE5T3WG4O%2F7X43w%2BMKbYwz7QQoE9AZMdkCc%2BXabxrE" \
          "%2FSn6mHKWoAj1F5hKPcOFKIkGds3zuBDm1ILyQkMMtL3IL5mD4fKRW5jq7t8RU669aHmNuYL%2FMBye8" \
          "%2FzAHK2c5SHNGt7kncrdqiOVqJfNFHyfhbap4tsCh7gmnZjPTGzgx8EM%2B6Qo71TrI%2BTODNEwGNuyyAQcNkx--lqAIWltrlbnvu3Xb" \
          "--bl4RgDDag3fM0ntF6DWQrw%3D%3D"
jar = requests.cookies.RequestsCookieJar()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}
for cookie in cookies.split(';'):
    key, value = cookie.split('=', 1)
    jar.set(key, value)
r = requests.get('https://www.github.com/', cookies=jar, headers=headers)
