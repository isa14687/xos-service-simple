#!/bin/bash
curl -H "xos-username: admin@opencord.org" -H "xos-password: letmein" -X POST --data-binary @$1 http://10.0.0.237:30007/run
