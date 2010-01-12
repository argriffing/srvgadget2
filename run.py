import argparse
import cherrypy


class MyForm:

    @cherrypy.expose
    def index(self):
        return 'hello'


def main(args):
    cherrypy.config.update({
        'server.socket_host': args.host,
        'server.socket_port': args.port})
    cherrypy.quickstart(MyForm())

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', type=str, default='127.0.0.1')
    parser.add_argument('--port', type=int, default=8080)
    main(parser.parse_args())
