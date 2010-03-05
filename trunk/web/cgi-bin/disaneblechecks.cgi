#!/bin/sh


# disable filename globbing
set -f

. /etc/profile > /dev/null 2>&1

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
EOF

cat << EOF

<TABLE BORDER="1">
<FORM METHOD=GET ACTION="/web/cgi-bin/cgidisaneblechecks.cgi">
  <CAPTION> Activation/D&eacute;sactivation des scenarii <INPUT type="submit" value="Appliquer"><INPUT type="reset" value="RaZ"></CAPTION>
  <TR>
 <TH> Nom du scenario </TH>
 <TH> Actif </TH>
 <TH> Inactif </TH>
  </TR>
EOF

for file in `ls $GRANDMAHOME/checks_available`
do
	echo "<TH>"
	echo "$file "
	echo "</TH>"
	if [ -e $GRANDMAHOME/checks_enabled/$file ]
	then
		echo "<TD><span style="color:green">Check actif</span></TD><TD><INPUT TYPE=radio NAME=$file VALUE=disable>Disable</TD>"
	else
		echo "<TD><INPUT TYPE=radio NAME=$file VALUE=enable>Enable</TD><TD><span style="color:red">Check inactif</span></TD>"
	fi
        echo "</TR>"
done
cat << EOF
</TABLE>
</body>
</html>
EOF
