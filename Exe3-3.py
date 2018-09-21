# #POST 방식으로 웹 서버에 요청 보내기
# from urllib.parse import urlencode
# from urllib.request import Request, urlopen
#
# data=urlencode({'name':'둘리','a':10,'b':20})
# print(data,'\n')
# data=data.encode("UTF-8") #바이트 형태로 보내야 하므로 인코딩 필요
# print(data)
#
# req=Request('http://www.example.com',data)
# req.add_header('Contest-Type','text/html')
#
# f = urlopen(req)
# req=f.read()
#
# print(req)

from urllib.parse import urlencode
from urllib.request import Request, urlopen

data = urlencode({'name':'둘리','email':'','pwd':''}) #join페이지에서 이부분에 빈공간으로 하고 for문을 돌리면 자동회원가입이 된다.
data = data.encode('UTF-8')

request = Request('http://www.example.com', data)
request.add_header('Content-Type', 'text/html')

f = urlopen(request)
response = f.read()
print(response)

f = urlopen(request)
response = f.read()
print(response)
