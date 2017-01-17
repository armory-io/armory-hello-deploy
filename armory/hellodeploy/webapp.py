from flask import Flask, render_template
import json
from armory.hellodeploy import kv_parser

server = Flask(__name__, static_url_path='/static')

@server.route("/")
def home():
    kv_text = open('/etc/default/server-env').read()
    env_kv = kv_parser.parse(kv_text)
    return render_template('index.html', userdata=env_kv)
