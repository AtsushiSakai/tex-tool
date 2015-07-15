#coding:utf-8
import os
from bottle import route, run, template, static_file, post, request

@route("/static/<filepath:path>")
def server_static(filepath):
    return static_file(filepath, root='static')

@route("/")
def index():
    return template("index")

if __name__ == '__main__':
    if os.getenv("HEROKU")==None:       
        run(host="localhost", port=(os.environ.get("PORT",5000)), debug=True, reloader=True)
    else:
        run(host="0.0.0.0", port=(os.environ.get("PORT",5200)))
