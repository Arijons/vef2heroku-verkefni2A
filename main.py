from sys import argv

import bottle
from bottle import*
bottle.debug(True)

@route('/')
def index():
    info = {'title': 'Welcome Home!',
            'content': 'Hello World'
            }

    return template('simple.tpl', info)


@route('/<name>')
def greet(name='Stranger'):
    return "Hello " + name




bottle.run(host="0.0.0.0", port=argv[1] )
