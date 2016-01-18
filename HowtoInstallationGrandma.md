#Howto Installation Grandma - Comment installer Grandma

# Introduction #

### Fonctionnel ###

  * Les sondes Grandma ont pour rôle d’exécuter des scénarii se déroulant sur des sites web ou applications _client léger_ afin d’en valider le bon fonctionnement.

  * Les données collectées par ces scénarii sont remontées vers Nagios
    * Statut du scénario (OK/KO)
    * Libellé d’erreur (Impossible de s’authentifier, etc. …)
    * Données de performance (Durée du scénario)

  * Grandma peut exécuter un nombre important de scénarii en parallèle (l’architecture technique actuelle limite leur nombre à 200, pour augmenter ce chiffre il est possible de multiplier les sondes Grandma)

  * Les scénarii sont exécutés toutes les minutes et l’information remontée en temps réel dans Nagios

  * Grandma gère les plages horaires spécifiques à chaque scénario afin de ne pas exécuter de contrôle sur les plages de maintenance et de traitement où l’application/site est indisponible de manière _normale_

  * Les informations peuvent être remontées en parallèle vers plusieurs serveurs nagios

  * En cas d’échec sur un scénario les données collectées (page générée, cookies etc. …) sont archivées afin de permettre l’analyse de l’incident

### Technique ###

Répertoire d’installation /opt/grandma

`/opt/grandma/arch` : répertoire de stockage des archives des scénarios en erreur

`/opt/grandma/cfg` : répertoire de configuration

`/opt/grandma/cfg/grandma.cfg` : configuration générale de l’application

`/opt/grandma/cfg/Grandma.cfg` : configuration spécifique à chaque sonde

`/opt/grandma/cfg/send_nsca*.cfg` : configuration des envois d’informations vers Nagios

`/opt/grandma/checks_available` : répertoire de stockage des scénarios

`/opt/grandma/checks_enabled` : répertoire des scripts activés sur la sonde (lien symbolique vers available)

`/opt/grandma/lib` : répertoire des scripts communs de l’application

`/opt/grandma/web` : répertoire des fichiers web (interface d’administration de grandma)

# Procédure d'installation #

Les applications à installer sur la sonde Grandma sont :

Client NSCA Linux (commande send\_nsca)

Grandma (tar.gz à télécharger)

## Installation de Grandma : ##

Décompresser le fichier grandma.tgz dans /opt/

Créer le user grandma utilisé par l’application

Changer les droits unix de /opt/grandma

Créer les liens symboliques permettant le démarrage de l’application (`ln -s /opt/grandma/lib/grandma /etc/init.d/grandma`)

Définir dans /etc/profile la variable `GRANDMAHOME="/opt/grandma"`

Mettre à jour les variables spécifiques à la sonde dans /opt/grandma/cfg/

Mettre en place les liens symboliques dans /opt/grandma/checks\_enabled

Mettre en place la crontab du user grandma assurant la purge des archives

# Intégration dans Nagios #

Les remontées d’informations depuis les sondes vers nagios se font via le protocole NSCA, à chaque scénario correspond un service **passif** sous nagios.

Un HOST virtuel Grandma doit être créé (adresse IP 127.0.0.1) et les services lui sont affectés.

Afin d’éviter des saisies répétitives des modèles nagios ont été créés. Le modèle generic-service\_grandma peut être appelé pour tous les services.

`# service de sonde passive nsca`

`define service{`
> `name                            generic-service_grandma ; The 'name' of this service template`

> `active_checks_enabled           0       ; Active service checks are enabled`

> `passive_checks_enabled          1       ; Passive service checks are enabled/accepted`

> `parallelize_check               1       ; Active service checks should be parallelized (disabling this can lead to major performance problems)`

> `obsess_over_service             1       ; We should obsess over this service (if necessary)`
> `check_freshness                 1       ; Default is to NOT check service 'freshness'`

> `notifications_enabled           1       ; Service notifications are enabled`

> `event_handler_enabled           1       ; Service event handler is enabled`

> `flap_detection_enabled          1       ; Flap detection is enabled`

> `failure_prediction_enabled      1       ; Failure prediction is enabled`

> `process_perf_data               1       ; Process performance data`

> `retain_status_information       1       ; Retain status information across program restarts`

> `retain_nonstatus_information    1       ; Retain non-status information across program restarts`

> `notification_interval           0               ; Only send notifications on status change by default.`

> `is_volatile                     0`

> `check_period                    24x7`

> `normal_check_interval           5`

> `retry_check_interval            1`

> `max_check_attempts              4`

> `notification_period             24x7`

> `notification_options            w,u,c,r`

> `contact_groups                  exploit-tr`

> `freshness_threshold             600`

> `check_command                   check_dummy_Grandma`

> `register                        0       ; DONT REGISTER THIS DEFINITION - ITS NOT A REAL SERVICE, JUST A TEMPLATE!`

> `}`

On ajoute aussi une commande **dummy** qui permet d'avoir une alerte nagios si la sonde Grandma ou Nsca plantent et qu'aucune information n'est remontée depuis 5 mn.

`define command{`

> `command_name    check_dummy_Grandma`

> `command_line    /opt/nagios/libexec/check_dummy 3 "KO : Pas d'information remontee par le serveur"`

`}`

Les services peuvent maintenant être ajoutés et doivent avoir cette forme **le nom du service doît être le même que le nom du scénario sur la sonde** :

`define service {`

> `host_name               Grandma`

> `service_description     check_site_*XXXX*`
> `use                     generic-service_grandma`
`}`

Le champ service\_description doit exactement correspondre au nom du scénario sur la machine grandma et sera donc toujours du type check\_site