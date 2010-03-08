#!/bin/sh
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


# disable filename globbing
set -f

. /etc/profile > /dev/null 2>&1

#echo Content-type: text/plain
echo Content-type: text/html
echo 


cat << EOF
<html>
<head>
  <title>IHM Surveillance des Applications - Grandma</title>
  <link rel="shortcut icon" type="image/x-icon" href="http://grandmatux.dummy.net:8080/web/favicon.ico">
</head>
<body>
<img alt="IMG" src="/web/dummy.jpg"><BR>
<BIG><BIG>AIDE</BIG></BIG>&nbsp;:&nbsp;Pour retrouver dans le scenario quel est le login utilis&eacute;, il faut chercher la ligne :<BR><BR>
source $GRANDMAHOME/lib/gestion_motdepasse.sh <B>000522895</B> ; if [ $? -eq 3 ]; then UNKNOWN "KO : Probleme lors de la recuperation des mots de passe"; fi
<BR><BR>
Le login utilis&eacute; par le scenario est affich&eacute; en gras, il faut le chercher dans la liste ci-dessous pour obtenir le mot de passe.
<BR><BR>
EOF

cat $GRANDMAHOME/lib/gestion_motdepasse.sh | grep "^.*:.*$" | grep -v " " | sed -e 's/:/<BR>Mot de passe :/' -e 's/^/Login : /' -e 's/$/<BR><BR>/'

cat << EOF
</body>
</html>
EOF
