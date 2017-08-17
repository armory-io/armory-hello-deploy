#!/bin/bash

DURATION=$1
HOST=$2

NOW=$(date +%s)
END_TIME=$(expr ${NOW} + ${DURATION} \* 60)

echo Running until ${END_TIME}

while [[ $(date +%s) -lt ${END_TIME} ]]; do
    RES=$(curl -q ${HOST}:5000/datadog/testrequest 2>/dev/null | wc -c)
    if [[ $? == 0 ]]; then
        echo "Got a ${RES} character response"
    else
        echo "Unable to fetch from ${HOST}"
    fi
done
