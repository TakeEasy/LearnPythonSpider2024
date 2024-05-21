import socket
from urllib import request, error

try:
    reponse = request.urlopen('https://cuiqingcai.com/404')
except error.HTTPError as e:
    print(e.reason, e.code, e.headers, sep='\n')
except error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')
    print(e.reason)
else:
    print('Request Successfully')
