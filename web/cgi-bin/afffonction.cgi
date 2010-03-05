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
  <CAPTION> Correspondance Sc&eacute;nario / Code Bo&icirc;te </CAPTION>
  <TR>
 <TH> Nom du scenario </TH>
 <TH> CODE CMDB </TH>
 <TH> CODE BOITE </TH>
 <TH> CODE LOGICIEL </TH>
  </TR>
EOF

for file in `ls $GRANDMAHOME/checks_enabled`
do
	echo "<TR>"
	echo "<TH>$file</TH>"
	echo "<TD>"
	grep "# URN" $GRANDMAHOME/checks_enabled/$file | sed -e 's/# URN//' -e 's/"//g' -e 's/^ //'
	echo "</TD>"
	echo "<TD>"
	codeboite=`grep "# CB" $GRANDMAHOME/checks_enabled/$file | sed -e 's/# CB//' -e 's/"//g' -e 's/^ //'`
	echo "<A HREF=http://cartographie.dummy.net:8080/cartographie/recherche.do?codeBoite=$codeboite target=mainFrame>$codeboite</A>"
	echo "</TD>"
	echo "<TD>"
	codelogiciel=`grep "# CL" $GRANDMAHOME/checks_enabled/$file | sed -e 's/# CL//' -e 's/"//g' -e 's/^ //'`
	echo "<A HREF=http://cartographie.dummy.net:8080/cartographie/initLogiciel.do?codeLogiciel=$codelogiciel target=mainFrame>$codelogiciel</A>"
	echo "</TR>"
done
cat << EOF
</TABLE>
</body>
</html>
EOF
