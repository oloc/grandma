#!/bin/sh


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
