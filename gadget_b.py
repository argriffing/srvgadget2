import random

import cherrypy


class MyForm:
    "Generate a random DNA sequence of the specified length."

    @cherrypy.expose
    def generate_random(self, length=None):
        n = int(length)
        if n < 1:
            raise ValueError('%d is too small' % n)
        if n > 1000:
            raise ValueError('%d is too large' % n)
        arr = [random.choice('acgt') for i in range(n)]
        return ''.join(arr)

    @cherrypy.expose
    def index(self):
        arr = [
                '<html><body>',
                '<form action="generate_random" method="post">',
                '<label for="length">length</label>',
                '<input type="text" id="length" name="length" />',
                '</form>'
                '</body></html>']
        return '\n'.join(arr)
