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
	echo "Probleme, pas de parametre passe - Syntaxe : $0 TRYPTIQUEB2B"
	exit 3
fi

if [ "$2" = "FORCE" ]
then
	echo -e "\n\nON FORCE LE LANCEMENT EN MODE MANUEL SANS TENIR COMPTE DE LA PLAGE HORAIRE\nATTENTION : L'INDISPONIBILITE D'UN SCENARIO PEUT ETRE NORMALE SUR CETTE PLAGE HORAIRE (TRAITEMENT EN COURS ETC...)\n\n"
	exit 0
fi

#         Lundi    :Mardi    :Mercredi :Jeudi    :Vendredi :Samedi   :Dimanche
# XXXX si controle permanent sur la journee
# NNNN si pas de controle sur la journee
#
PROFIL_1="0001:2300:0600:2300:0600:2300:0600:2300:0600:2300:0600:2359:XXXX:XXXX"
PROFIL_2="0001:2300:0500:2300:0500:2300:0500:2300:0500:2300:0500:2359:XXXX:XXXX"
# Intranet etendu
PROFIL_3="0735:1930:0735:1930:0735:1930:0735:1930:0735:1930:0735:1730:NNNN:NNNN"
# Internet
PROFIL_4="XXXX:XXXX:XXXX:XXXX:XXXX:XXXX:XXXX:XXXX:XXXX:XXXX:XXXX:XXXX:XXXX:XXXX"
# L au V 8h>18h
PROFIL_5="0745:1800:0745:1800:0745:1800:0745:1800:0745:1800:NNNN:NNNN:NNNN:NNNN"
# Intranet L au V 8h>18h S 8h>13h
PROFIL_6="0745:1800:0745:1800:0745:1800:0745:1800:0745:1800:0745:1300:NNNN:NNNN"
# Specifique EAB
PROFIL_7="0800:2200:0800:2200:0800:2200:0800:2200:0800:2200:0900:1400:NNNN:NNNN"

valeurs=`cat << EOF | grep -v "^#" | grep $1
FTN:$PROFIL_2
EOF`

if [ `echo $valeurs | grep -c $1` -ne 1 ]
then
	echo "Probleme, le client est introuvable"
	exit 3
fi

heure=`date +%H%M`
#heure="$2"
jour=`date '+%a'`
#jour="$3"

# scenario suspendu 2 fois = Bascule CICZ en mode nuit puis en mode jour
if [ "$1" = "FTN" ] && [ $heure -ge 1958 ] && [ $heure -le 2015 ]
then
	exit 1
fi

if [ "$jour" = "lun" ]
then
	debut=`echo $valeurs | awk -F : '{print $2}'`
	fin=`echo $valeurs | awk -F : '{print $3}'`
fi
if [ "$jour" = "mar" ]
then
	debut=`echo $valeurs | awk -F : '{print $4}'`
	fin=`echo $valeurs | awk -F : '{print $5}'`
fi
if [ "$jour" = "mer" ]
then
	debut=`echo $valeurs | awk -F : '{print $6}'`
	fin=`echo $valeurs | awk -F : '{print $7}'`
fi
if [ "$jour" = "jeu" ]
then
	debut=`echo $valeurs | awk -F : '{print $8}'`
	fin=`echo $valeurs | awk -F : '{print $9}'`
fi
if [ "$jour" = "ven" ]
then
	debut=`echo $valeurs | awk -F : '{print $10}'`
	fin=`echo $valeurs | awk -F : '{print $11}'`
fi
if [ "$jour" = "sam" ]
then
	debut=`echo $valeurs | awk -F : '{print $12}'`
	fin=`echo $valeurs | awk -F : '{print $13}'`
fi
if [ "$jour" = "dim" ]
then
	debut=`echo $valeurs | awk -F : '{print $14}'`
	fin=`echo $valeurs | awk -F : '{print $15}'`
fi

if [ "$debut" = "XXXX" ] || [ "$fin" = "XXXX" ]
then
	exit 0
fi
if [ "$debut" = "NNNN" ] || [ "$fin" = "NNNN" ]
then
	exit 1
fi

if [ $heure -ge $debut ] && [ $heure -le $fin ]
then
	exit 0
else
	exit 1
fi
