import http.server
import socketserver
PORT=900
Handler=httpserver.SimpleHTTPRequestHandler
with socketserver.TCPServer((1111,PORT),Handler)as httpd:
    print("serving at port",PORT)
    httpd.server_forever()
    