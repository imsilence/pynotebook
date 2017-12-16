#encoding: utf-8

from flask import Flask
from flask import url_for
from flask import request
from flask import render_template
from flask import make_response
from flask import redirect
from flask import session
from flask import flash

from utils import load_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/hello', methods=["get", "post"])
def hello():
    print request.method
    return 'hello'

@app.route('/name/<name>/')
def name(name):
    return 'hello, %s' % name

@app.route('/name/<name>/<int:age>/')
def age(name, age):
    return 'hello, %s, %s' % (name, age)

@app.route('/url/')
def url():
    return url_for('name', name='kk', age=29)


@app.route('/html/')
@app.route('/html/<username>/')
@app.route('/html/<username>/<password>/')
def html(username='', password=''):
    _html = '''
    <!DOCTYP html>
        <head>
            <meta charset="utf-8"/>
            <title>XXX</title>
        </head>
        <body>
            <form>
                <label>名称:</label><input name="username" type="text" value="{username}"/><br/>
                <label>密码:</label><input name="password" type="password" value="{password}"/><br/>
            </form>
        </body>
    </html>
    '''
    return _html.format(username=username, password=password)

@app.route('/html2/')
@app.route('/html2/<username>/')
@app.route('/html2/<username>/<password>/')
def html2(username='', password=''):
    return load_template('hello.html').format(username=username, password=password)

@app.route('/html3/')
@app.route('/html3/<username>/')
@app.route('/html3/<username>/<password>/')
def html3(username='', password=''):
    return render_template('hello3.html', username=username, password=password)

@app.route('/login/', methods=["get", "post"])
def login():
    return str(request.form) if request.method=='POST' else str(request.args)

@app.route('/glogin/', methods=["get"])
def glogin():
    return str(request.args)

@app.route('/plogin/', methods=["post"])
def plogin():
    return str(request.form) 

@app.route('/upload/', methods=["post"])
def upload():
    _file = request.files.get('image', None)
    if _file:
        print _file.stream.read()
        #_file.save("e:/t.txt")
        return 'success'
    return 'error'

@app.route('/setcookie/<key>/<value>/')
def setcookie(key, value):
    reponse = make_response()
    reponse.set_cookie(key, value)
    return reponse

@app.route('/getcookie/')
def getcookie():
    return str(request.cookies)

@app.route('/redirect/')
def rd():
    return redirect(url_for('index'))

@app.errorhandler(404)
def not_found(error):
    return 'i don\' know what you say!', 200, {'found':'false'}

@app.route('/setsession/<key>/<value>/')
def setsession(key, value):
    app.logger.debug('set session %s:%s', key, value)
    session[key] = value
    return 'session'

@app.route('/getsession/<key>/')
def getsession(key):
    print session
    return str(session.get(key))

@app.route('/logs')
def logs():
    logs = []
    flash('tip')
    '''
    with open('data.txt') as h:
        for line in h:
            logs.append(eval(line))
    '''
    return render_template('logs.html', logs=logs)


app.secret_key = "\x8cq\xd6\xd7'\xecm\x1a\xa1\x8cL\x1d`\xb8\xd6\xa5\x19B\x92\xf9\xef\xd2\x8dg"


if __name__ == '__main__':
    app.run(debug=True)