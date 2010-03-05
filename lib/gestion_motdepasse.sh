#!/bin/bash

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
