
## Ajuster l'horloge du système

Ubuntu a longtemps utilisé `ntpdate` et `ntpd` pour ajuster l'horloge interne des systèmes d'exploitation, 
cette tâche est désormais assurée par `timedatectl` qui est installé par défaut dans votre distribution.

| ancien | nouveau | commentaire |
| ---    | ---     | ---         |
| ntpdate | timedatectl | client ntp | 
| ntpd (partie client) | timesyncd | | 

## Timesyncd
`timesyncd` se substitue à la partie client de `ntpd`.   
`timesync` vérifie l'heure de référence à intervalles réguliers et assure le maintien de la synchronisation des horloges.   
Il effectue également le stockage local des synchronisations, ainsi leur prise en compte est assurée en cas de réinitialisation.  

## timedatectl 
donne la conf actuelle de l'heure  
`timedatectl status`
