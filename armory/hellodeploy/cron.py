#!/usr/bin/env python3

from apscheduler.schedulers.background import BackgroundScheduler
from armory.hellodeploy import kv_parser
from random import randint

import datadog
import logging

sched = BackgroundScheduler()


def start():

    print("Checking if heartbeat should run.")
    try:
        with open('/etc/default/server-env', 'r') as f:
            vars = kv_parser.parse(f.read())
            print(vars)
            if 'CLOUD_DETAIL' in vars:
                if 'canary' in vars['CLOUD_DETAIL'] or 'baseline' in vars['CLOUD_DETAIL']:
                    print("heartbeating enabled.")
                    sched.add_job(heartbeat, 'interval',
                                  seconds=10, id='heartbeat')
                    sched.start()
                else:
                    print("Heartbeat should not be enabled.")
    except FileNotFoundError:
        logger.error("Could open server-env and start heartbeat.")


def heartbeat():
    num = randint(95, 105)
    print("heartbeating %d" % num)
    datadog.dogstatsd.statsd.gauge("hellodeploy.heartbeat", num)
