from flask import Flask, render_template, jsonify
import json
from armory.hellodeploy import kv_parser
import datadog


server = Flask(__name__, static_url_path='/static')

datadog_options = {
    'api_key':'71120e33fa59c2bf8af09b6d881344b4',
    'app_key':'hellodeploy'
}

datadog.initialize(**datadog_options)


@server.route("/")
def home():
    kv_text = open('/etc/default/server-env').read()
    env_kv = kv_parser.parse(kv_text)
    return render_template('index.html', userdata=env_kv)


@server.route("/datadog/event")
def datadog_warn():
    datadog.dogstatsd.statsd.event('Warn Button', 'someone clicked the button')

    return jsonify({"sent": "warning event"})



@server.route("/datadog/counter")
def datadog_counter():
    datadog.dogstatsd.statsd.increment("hellodeploy.buttons.datadog.warning")

    return jsonify({"sent": "counter increment"})
