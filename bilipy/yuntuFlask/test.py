# -*-coding:utf-8-*-

import json
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
# from config import devcfg
import re
# from dingTalk import sendmsg

import logging

from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, options

define('port', type=int, default=80)
# deploy or debug
define('mode', default='debug')

def getDirs(path):
    for root, dirs, files in os.walk(path):
        return root, files

app = Flask(__name__)

@app.route('/')
def index():
    root, files = getDirs('static/')
    img_urls = []
    for file in files:
        img_urls.append(root+file)
        print(files)
    return render_template('index.html', img_urls=img_urls)

def main():
    options.parse_command_line()
    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(options.port)
    logging.warn("[UOP] App is running on: localhost:%d", options.port)
    IOLoop.instance().start()

if __name__ == '__main__':
    main()
    # app.run(host='0.0.0.0', port=8111)
