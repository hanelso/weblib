# 장고를 쓰기 전에 웹서버 간단한 프레임 워크를 진행했다.
# 웹 서버의 기능을 해주는 뼈대는 이렇게 되어있다.
# 일단 익숙해 지기 전에 이것을 분석하는것은 위험...

from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs

port = 7777


class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    def get_params(self,name):
        qs = self.path[self.path.find('?')+1:]
        params = parse_qs(qs)
        values = params.get(name)
        #params와 values의 값을 확인
        print(type(values), type(params))
        print(values, params)


        return "" if values is None else values.pop()
        #같은 의미의 구문.
        # if values is None:
        #     return None
        # else:
        #     return values.pop()
    def ex1(self):
        self.send_response(200)  # 서버에서 응답해주는 부분
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write("<h1>EX1 Fuction</h1>".encode("utf-8"))

    def ex2(self):
        self.send_response(200)  # 서버에서 응답해주는 부분
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write("<h1>EX2 Fuction</h1>".encode("utf-8"))

    def do_GET(self):
        index = self.path.find('?')
        req_url = self.path if index == -1 else self.path[:index]


        #URL MAPPING
        if req_url == "/iot":
            handler_name = 'ex' + self.get_params('ex')
        #    print(handler_name)
            if handler_name not in MyHTTPRequestHandler.__dict__:
                self.send_error(404,"File Not Found")
                return

            MyHTTPRequestHandler.__dict__[handler_name](self)

        elif req_url == '/board':
            pass
        else:
            self.send_error(404, "File Not Found")




httpd = HTTPServer(("",port),MyHTTPRequestHandler)
print("Server running on port", port)
httpd.serve_forever()


#http://localhost:777/iot?ex=1
#http://localhost:777/iot?ex=2
#http://localhost:777/iot?ex=3