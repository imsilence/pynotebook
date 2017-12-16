#encoding : utf-8

from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/commit/', methods=["POST", "GET"])
def commit():
    print request.args
    print request.form.getlist('hobby')
    print request.form.getlist('gender')
    print request.headers.get('Content-Type')
    _img = request.files.get('img')
    print _img.name
    print _img.filename
    _img.save('e:/1')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=9001, debug=True)
