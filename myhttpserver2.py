from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs

port = 7777


class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    def get_params(self,name):
        qs = self.path[self.path.find('?')+1:]
        params = parse_qs(qs)
        values = params.get(name)

        return values.pop()

    def do_GET(self):
        req_url = self.path[:self.path.find('?')]

        #URL MAPPING
        if req_url=='/iot':
            value = self.get_params('ex')
            self.send_response(200)     #서버에서 응답해주는 부분
            self.send_header("Content-Type","text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write("<h1>TEST</h1>".encode("utf-8"))
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