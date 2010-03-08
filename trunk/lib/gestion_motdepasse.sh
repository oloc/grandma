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

export LANG=fr_FR@euro

if [ $# -lt 1 ]
then
	echo "Probleme, pas de parametre passe - Syntaxe : $0 utilisateur"
	exit 3
fi

DDMMYYY=`date '+%d%m%Y'`

valeurs=`cat << EOF | grep -v "^#" | grep "^$1:"
123456:123456
EOF`

if [ `echo $valeurs | grep -c $1` -ne 1 ]
then
	echo "Probleme, l'utilisateur est introuvable"
	exit 3
fi

motdepasse=`echo $valeurs | awk -F : '{print $2}'`
export motdepasse=$motdepasse
