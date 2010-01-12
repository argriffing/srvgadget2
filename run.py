import sys
import os

import argparse
import cherrypy

g_script_path = os.path.abspath(sys.argv[0])
g_script_directory = os.path.dirname(g_script_path)

sys.path.append(g_script_directory)


class MyForm(object):

    def __init__(self):
        self.modules = []

    def add_module(self, m):
        self.modules.append(m)
        setattr(self, m.__name__, m.MyForm())

    @cherrypy.expose
    def index(self):
        arr = []
        arr.append('<html><body>')
        arr.append('<code>')
        for m in self.modules:
            link = '[<a href="%s">cgi</a>]' % m.__name__
            arr.append(link)
            arr.append(m.MyForm.__doc__)
            arr.append('<br />')
        arr.append('</code>')
        arr.append('</body></html>')
        return '\n'.join(arr)


def main(args):
    cherrypy.config.update({
        'server.socket_host': args.host,
        'server.socket_port': args.port})
    myform = MyForm()
    module_names = []
    modules = []
    for filename in os.listdir(g_script_directory):
        if filename.startswith('gadget_'):
            module_name, extension = os.path.splitext(filename)
            if extension == '.py':
                module_names.append(module_name)
                module = __import__(module_name)
                modules.append(module)
    for module in modules:
        print 'gadget form docstring:', module.MyForm.__doc__
        myform.add_module(module)
    cherrypy.quickstart(myform)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', type=str, default='127.0.0.1')
    parser.add_argument('--port', type=int, default=8080)
    main(parser.parse_args())
