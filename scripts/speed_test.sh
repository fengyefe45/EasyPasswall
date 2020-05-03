#!/bin/bash
DIR=$(cd $(dirname $0) && pwd )
timeout 10 ping -c4 baidu.com | grep '^rtt' | awk -F"/" '{print $5F}' | tee $DIR/logs/ping_baidu.log
timeout 10 ping -c4 google.com | grep '^rtt' | awk -F"/" '{print $5F}'| tee $DIR/logs/ping_google.log
