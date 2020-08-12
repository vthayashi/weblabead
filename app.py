# python app.py
# https://github.com/arshadansari27/flask-image-server/blob/master/app.py
# http://zetcode.com/python/flask/

from flask import Flask, send_file, abort, make_response
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    filename = 'index.htm'
    return send_file(filename, mimetype='text/html')

@app.route('/Motor6.htm')
def motor6():
    filename = 'Motor6.htm'
    return send_file(filename, mimetype='text/html')

@app.route('/Motor6b.htm')
def motor6b():
    filename = 'Motor6b.htm'
    return send_file(filename, mimetype='text/html')

@app.route("/data/<path:path>")
def data(path):
    filename = 'data/'+path
    try:
        return send_file(filename, mimetype='text/json')
    except FileNotFoundError:
        abort(404)

@app.route("/html/<path:path>")
def html(path):
    filename = 'html/'+path
    try:
        return send_file(filename, mimetype='text/html')
    except FileNotFoundError:
        abort(404)

@app.route('/list')
def list():
    filename = 'list.txt'
    return send_file(filename, mimetype='text/json')
    
    return data

@app.route('/logo.png')
def logo():
    filename = 'logo.png'
    return send_file(filename, mimetype='image/jpeg')

if __name__ == '__main__':
    #app.run(host="127.0.0.1", port=5000)
    app.run(host="127.0.0.1", port=80)
