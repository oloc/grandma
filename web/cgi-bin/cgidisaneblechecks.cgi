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

echo Content-type: text/html
echo 

cat << EOF
<html>
<META HTTP-EQUIV="Refresh" CONTENT="2; URL=/web/cgi-bin/disaneblechecks.cgi"> 
<body>
EOF
check=`echo $QUERY_STRING | awk -F = '{print $1 }'`
query=`echo $QUERY_STRING | awk -F = '{print $2 }'`
if [ "$check" = "" ]
then
cat << EOF
<center><B>Probleme dans le CGI</B></center>
EOF
exit 0
fi
if [ "$query" = "disable" ]
then
	echo "Desactivation ...<BR>"
	rm -vf $GRANDMAHOME/checks_enabled/$check 1> /dev/null 2>&1
	if [ $? -ne 0 ]; then echo "Probleme lors de la d&eacute;sactivation !"; else echo "$check est d&eacute;sactiv&eacute;"; fi
else
	echo "Activation ...<BR>"
	cd $GRANDMAHOME/checks_enabled ; ln -vs ../checks_available/$check $check 1> /dev/null 2>&1
	if [ $? -ne 0 ]; then echo "Probleme lors de l'activation !"; else echo "$check est activ&eacute;"; fi
fi
cat << EOF
</body>
</html>
EOF
