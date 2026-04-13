from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(length).decode() if length else ''
        print('收到请求体:', body)
        # 原样返回
        resp = {'received': body}
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(resp).encode())

if __name__ == '__main__':
    HTTPServer(('127.0.0.1', 8000), Handler).serve_forever()
