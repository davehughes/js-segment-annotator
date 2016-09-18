#!/usr/bin/env python
from __future__ import print_function
import argparse
import SimpleHTTPServer
import SocketServer
import sys


def parse_opts(argv=None):
    argv = argv or sys.argv[1:]
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    # serve subcommand
    def cmd_serve(opts):
        Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
        httpd = SocketServer.TCPServer(("", opts.port), Handler)
        print("Serving at port {}. Press <C-c> to stop.".format(opts.port))
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("Received keyboard interrupt, exiting.")
            sys.exit(0)

    serve_cmd = subparsers.add_parser('serve')
    serve_cmd.add_argument('--port', type=int, default=8000)
    serve_cmd.set_defaults(func=cmd_serve)

    return parser.parse_args(argv)


def main():
    opts = parse_opts()
    return opts.func(opts)


if __name__ == '__main__':
    main()
