# Chrony
installation : `sudo apt install chrony`  
Fichier de config : `/etc/chrony/chrony.conf`  
vérifier l'exécution du service : `sudo systemctl status chronyd`  
redémarrer : `sudo systemctl restart chronyd`  

Vérifier qu'une adresse du réseau est bien autorisée à accéder au server NTP chrony (d'après la conf allow/deny du fichier de conf) :
`sudo chronyc accheck 192.168.0.1`  

Statut :  
```
chronyc sources -v 
chronyc tracking  
chronyc activity



```

Pour configurer en tant que server :  
```
# Configuration en tant que serveur NTP (pour réseau local)
deny all
allow 192.168.0.0/24
local stratum 10
```

pour configurer les logs:
```
# log
log tracking measurements statistics
```



## Ajuster l'horloge du système

Ubuntu a longtemps utilisé `ntpdate` et `ntpd` pour ajuster l'horloge interne des systèmes d'exploitation, 
cette tâche est désormais assurée par `timedatectl` qui est installé par défaut dans votre distribution.

| ancien | nouveau | commentaire |
| ---    | ---     | ---         |
| ntpdate | timedatectl | client ntp | 
| ntpd (partie client) | timesyncd | sudo apt install -V systemd-timesyncd | 

/!\ Si ntpdate ou ntpd sont installés, timedatectl se désactive pour permettre à l'utilisateur d'utiliser l'ancienne configuration. -> vérifier que ces anciens services ne sont pas installés.

## client NTP : Timesyncd / timedatectl 
`timesyncd` se substitue à la partie client de `ntpd`.   
`timesync` vérifie l'heure de référence à intervalles réguliers et assure le maintien de la synchronisation des horloges.   
Il effectue également le stockage local des synchronisations, ainsi leur prise en compte est assurée en cas de réinitialisation.  
installation `sudo apt install -V systemd-timesyncd`  

Vérifier que le service est actif : `systemctl status systemd-timesyncd.service`  
Fichier de conf: `/etc/systemd/timesyncd.conf`  copié dans `/etc/systemd/timesyncd.conf.d/toto` 
Vérifier l'ensemble des fichiers de config: `systemd-analyze cat-config systemd/timesyncd.conf`  
Vérifier la conf actuelle de l'heure  
`timedatectl status`  
`timedatectl timesync-status`  
Activer la synchronisation: `timedatectl set-ntp true`  
`Choisir un fuseau horaire: timedatectl set-timezone Europe/Paris`  

## Configuration du serveur /etc/ntpd.conf
Restreindre les requêtes au réseau local:  

`restrict 192.168.0.0 mask 255.255.255.0 nomodify notrap`  

# Test
Un moyen simple de voir s'il y a un broadcast NTP dans votre réseau local (généralement le router). A noter que le serveur n'est pas forcément configuré en broadcast, ça peut être les clients locaux qui sont configurés en pooling (en général).  
`sudo tcpdump -n "broadcast or multicast" | grep NTP`  

Pour voir si des clients se connectent à votre serveur NTP :
`ntpq -c mrulist`

  


