import cherrypy


class MyForm:
    "Take the reverse complement of a strand of DNA."

    @cherrypy.expose
    def reverse_complement(self, dna=None):
        d = {'a':'t', 't':'a', 'c':'g', 'g':'c'}
        arr = [d.get(c, c) for c in reversed(dna.lower())]
        return ''.join(arr)

    @cherrypy.expose
    def index(self):
        arr = [
                '<html><body>',
                '<form action="reverse_complement" method="post">',
                '<label for="dna">DNA</label>',
                '<input type="text" id="dna" name="dna" />',
                '</form>'
                '</body></html>']
        return '\n'.join(arr)
