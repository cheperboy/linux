
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

## Configuration du serveur /etc/ntpd.conf
Restreindre les requêtes au réseau local:  

`restrict 192.168.0.0 mask 255.255.255.0 nomodify notrap`  

# Test
Un moyen simple de voir s'il y a un broadcast NTP dans votre réseau local (généralement le router). A noter que le serveur n'est pas forcément configuré en broadcast, ça peut être les clients locaux qui sont configurés en pooling (en général).  
`sudo tcpdump -n "broadcast or multicast" | grep NTP`  

Pour voir si des clients se connectent à votre serveur NTP :
`ntpq -c mrulist`

  


