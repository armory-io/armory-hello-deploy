#!/usr/bin/env python3
from flask import Flask
from armory.hellodeploy.webapp import server
from armory.hellodeploy.cron import start
import signal


def term_handler(signal, frame):
    print("caught sigterm")
    term_func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    term_func()

signal.signal(signal.SIGTERM, term_handler)

if __name__ == "__main__":
    start()
    server.run(debug=True, host='0.0.0.0', threaded=True)
