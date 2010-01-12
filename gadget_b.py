import random

import cherrypy


class MyForm:
    "Generate a random DNA sequence of the specified length."

    @cherrypy.expose
    def generate_random(self, length_string=None):
        n = int(length_string)
        arr = [random.choice('acgt') for i in range(n)]
        return ''.join(arr)

    @cherrypy.expose
    def index(self):
        arr = [
                '<html><body>',
                '<form action="generate_random" method="post">',
                '<label for="length_string">length</label>',
                '<input type="text" id="length_string" name="length_string" />',
                '</form>'
                '</body></html>']
        return '\n'.join(arr)
