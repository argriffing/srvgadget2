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
            name = m.__name__
            link = '[<a href="%s">cgi</a>]' % m.__name__
            doc = '[<a href="doc/%s-pysrc.html">src</a>]' % m.__name__
            arr.append(name)
            arr.append(link)
            arr.append(doc)
            arr.append(m.MyForm.__doc__)
            arr.append('<br />')
        arr.append('</code>')
        arr.append('</body></html>')
        return '\n'.join(arr)

def get_static_conf():
    current_directory = os.path.abspath(os.curdir)
    doc_directory = os.path.join(current_directory, 'html')
    conf = {'/doc': {
        'tools.staticdir.on': True,
        'tools.staticdir.dir': doc_directory}}
    return conf

def create_documentation():
    epy_source = os.path.join(g_script_directory, '*.py')
    epy_cmd = ' '.join(['epydoc', epy_source])
    os.system(epy_cmd)

def main(args):
    cherrypy.config.update({
        'server.socket_host': args.host,
        'server.socket_port': args.port})
    myform = MyForm()
    module_names = []
    for filename in os.listdir(g_script_directory):
        if filename.startswith('gadget_'):
            module_name, extension = os.path.splitext(filename)
            if extension == '.py':
                module_names.append(module_name)
    for module_name in sorted(module_names):
        module = __import__(module_name)
        myform.add_module(module)
    create_documentation()
    cherrypy.quickstart(myform, '/', config=get_static_conf())

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', type=str, default='127.0.0.1')
    parser.add_argument('--port', type=int, default=8080)
    main(parser.parse_args())
