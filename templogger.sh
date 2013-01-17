#!/bin/bash

YR=$(date '+%H-%M-%S:%m-%d-%y:')
YS=$(/opt/vc/bin/vcgencmd measure_temp | awk '{ print (substr($1,6,4)) }')
echo $YR$YS >> /tmp/logs/templog

