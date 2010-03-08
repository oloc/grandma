#!/bin/bash
#
#Copyright 2002,2010 - Antoine Theuret
#
#This file is part of Grandma.
#
#Grandma is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#any later version.
#
#Grandma is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with Grandma.  If not, see <http://www.gnu.org/licenses/>.
#

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
