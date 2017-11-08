#!/bin/ssh

cat > /etc/newrelic-infra.yml <<EOF
license_key: 001107cdaf3230d77288b1d1634cfe9dd669802c
EOF
service newrelic-infra restart

# nrsysmond-config --set license_key=001107cdaf3230d77288b1d1634cfe9dd669802c
# service newrelic-sysmond restart

newrelic-admin generate-config 001107cdaf3230d77288b1d1634cfe9dd669802c /etc/newrelic.ini
sed -i 's/Python Application/armoryhellodeploy/' /etc/newrelic.ini
service armory-hello-deploy restart
