#HTTP 서버 제작
from http.server import BaseHTTPRequestHandler, HTTPServer

port = 8888

class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    def get_params(self, name):
        return

    def do_GET(self):
        name_handler = self.path[:self.path.index('?')]
#수정중
        # if name_handler == "/iot":
        #     value = get_params(self.path[self.path.find('?')]:)
        #     pass
        # elif name_handler == "/board":
        #     pass
        # else:
        #     pass

        self.send_response(200)     #서버에서 응답해주는 부분
        self.send_header("Content-Type","text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write("<h1>안녕하세요!</h1>".encode("utf-8"))

# class Server{ } -> 자바의 경우
# class Server: pass -> 파이선의 경우



httpd = HTTPServer(("",port),MyHTTPRequestHandler)
print("Server running on port", port)
httpd.serve_forever()
