#!/usr/bin/env python3

import time

import datadog

from armory.hellodeploy import kv_parser


datadog_options = {
    'api_key':'71120e33fa59c2bf8af09b6d881344b4',
    'app_key':'hellodeploy'
}

datadog.initialize(**datadog_options)

def main():
    try:
        kv_text = open('/etc/default/server-env').read()
    except FileNotFoundError:
        kv_text = open('etc/server-env').read()

    env_kv = kv_parser.parse(kv_text)

    if "CANARYERRORS" not in env_kv:
        return

    # Loop because DataDog doesn't reliably tag the events with ASG,
    # so the monitor doesn't have that info when it alerts,
    # and Barometer can't tell which canary to fail.

    asg = env_kv["CLOUD_SERVER_GROUP"][1:-1]
    tags = ["#autoscaling_group:%s" % asg]

    while True:
        for _ in range(5):
            datadog.dogstatsd.statsd.event('CanaryTest', 'canarytest: autoscaling_group:%s' % env_kv["CLOUD_SERVER_GROUP"], tags=tags)

        print("Delivered 5 CanaryTest events to datadog.")
        time.sleep(120)


if __name__ == "__main__":
    main()
