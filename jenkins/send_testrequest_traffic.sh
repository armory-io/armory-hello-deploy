#!/bin/bash

if [[ $# -lt 2 ]]; then
  echo "Usage: $0 DURATION HOST"
  exit 1
fi

DURATION=$1
HOST=$2
BASE_URL=http://${HOST}
NOW=$(date +%s)
END_TIME=$(expr ${NOW} + ${DURATION} \* 60)

echo Running until ${END_TIME}

call_url() {
  URL=$1
  RES=$(curl -q ${URL} 2>/dev/null | wc -c)
  if [[ $? == 0 ]]; then
    echo "Got a ${RES} character response for url: ${URL}"
  else
    echo "Unable to fetch from ${HOST}"
  fi
}

while [[ $(date +%s) -lt ${END_TIME} ]]; do
  call_url ${BASE_URL}/datadog/testrequest
  call_url ${BASE_URL}/datadog/counter?tag=subsystem:api
  if [[ $(($(date +%s) % 5)) -eq 0 ]]; then
    # this is just to confirm that filtering on tags is working correctly by
    # adding a few metrics with a different tag
    call_url ${BASE_URL}/datadog/counter?tag=subsystem:ui
  fi
done
