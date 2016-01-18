**Grandma** est une sonde robotisée, elle exécute à intervalles réguliers des scénarii permettant de simuler l'action d'un utilisateur sur une application. Chaque étape du scénario fait l'objet d'une vérification pour valider que la réponse de l'application est satisfaisante.

**Grandma** permet de simuler ces actions sur toute application web, 3270, OpenVMS et Unix (tout ce qui n'est pas client lourd en fait). Elle utilise pour cela les outils GNU : cUrl, c3270, Expect et est écrite en Bash.

**Grandma** prend en charge un calendrier et des profils de scénarii afin de gérer les plages de maintenance et adapter les contrôles aux plages d'activité des applications.

**Grandma** fait office de collecteur/ordonnanceur. Une fois les résultats (scénario terminé avec succès, temps d'exécution) récupérés, l'information est remontée vers Nagios à l'aide du client Nsca.

Si on utilise l'event broker ndoutils, l'ensemble des données (statut et performance du scénario) est historisé dans une base mysql que l'on peut utiliser pour faire de la métrologie ou du capacity planning.

**Grandma** existe depuis 4 ans sous sa forme actuelle, et 8 ans si l'on compte les premiers balbutiements. Sans parler de "solution complète", car elle est encore très rustique, Grandma est mature et utilisée depuis 9 mois en production pour des entreprises.