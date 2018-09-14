from sys import argv

import bottle
from bottle import*
bottle.debug(True)

from bottle import Bottle, template




@route('/')
def index():
    """Home page"""

    info = {'title': 'Welcome Home!',
            'content': 'Hello World'
            }

    return template('simple.tpl', info)


@route('/<name>')
def greet(name='Stranger'):
    return "Hello " + name




bottle.run(host="0.0.0.0", port=argv[1] )
