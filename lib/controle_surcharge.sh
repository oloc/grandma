#!/bin/bash

brut=`cut -f 2 -d " " /proc/loadavg` ; load=${brut%%.*}

if [ $load -gt 20 ]
then
	exit 3
else
	exit 0
fi
