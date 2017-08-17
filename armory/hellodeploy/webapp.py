# -*- Python -*_

# pylint: disable=invalid-name

# System modules
import os
from subprocess import call
import time

# 3rd party modules
import datadog
from flask import Flask, render_template, jsonify

# Our stuff
from armory.hellodeploy import kv_parser


server = Flask(__name__, static_url_path='/static')

datadog_options = {
    'api_key': '71120e33fa59c2bf8af09b6d881344b4',
    'app_key': 'hellodeploy'
}

datadog.initialize(**datadog_options)


@server.route("/")
def home():
    kv_text = open('/etc/default/server-env').read()
    env_kv = kv_parser.parse(kv_text)
    build_data = kv_parser.parse(
        open('/etc/default/armory-hello-deploy').read())
    return render_template('index.html', build_data=build_data, userdata=env_kv)


@server.route("/datadog/event")
def datadog_warn():
    datadog.dogstatsd.statsd.event('Warn Button', 'someone clicked the button')

    return jsonify({"sent": "warning event"})


@server.route("/datadog/counter")
def datadog_counter():
    datadog.dogstatsd.statsd.increment("hellodeploy.buttons.datadog.warning")

    return jsonify({"sent": "counter increment"})


@server.route("/datadog/shutdown_canary")
def datadog_shutdown_canary():
    os.system("inject_canary_errors.py --force &")
    return jsonify({"sent": "ok"})

@server.route("/datadog/testrequest")
def datadog_testrequest():
    """ This is used to drive a metrics test using the automated canary
    analysis function in Barometer. Depending on the "Detail" field set in the
    Spinnaker cluster used to deploy this server, this endpoint will either
    return a very small or a much larger payload. We then use the network
    bytes out for the machine as a metric to drive the canary evaluation.
    """
    kv_text = open('/etc/default/server-env').read()
    env_kv = kv_parser.parse(kv_text)
    payload = ""
    if ("CLOUD_DETAIL" in env_kv and env_kv["CLOUD_DETAIL"] == "fail-canary"):
        payload = "x" * 1000
    return jsonify({"payload": payload})

@server.route("/increase_disk")
def add_disk():
    call(["dd", "if=/dev/zero", "of=/tmp/filler-file-" +
          str(int(time.time() * 1000)), "bs=1M", "count=512"])
    return jsonify({"sent": "ok"})
