#!/bin/bash

# Creation des repertoires de travail
mkdir $tmpdir 1> /dev/null 2>&1
if [ $? -ne 0 ]
then
	exit 3
fi

# On flagge le debut du scenario pour collecter les donnees de performance
date '+%s.%N' > $tmpdir/timestamp
if [ $? -ne 0 ]
then
	exit 3
fi
exit 0
