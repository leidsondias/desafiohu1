# -*-coding: utf-8 -*-

import SimpleHTTPServer
import SocketServer
import os

PORT = 8000

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
os.chdir("site/")
httpd.serve_forever()
