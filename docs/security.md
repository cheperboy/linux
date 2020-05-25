## General links
- [raspberry.org - basic security](https://www.raspberrypi.org/documentation/configuration/security.md)
- [pestmeester.nl - complete guide including ssl certificate and ssh-keygen](http://pestmeester.nl/)
- [debian.org - securing-debian-howto](https://www.debian.org/doc/manuals/securing-debian-howto/ch-sec-services.fr.html)
- [debian.org - evaluation des vulnérabilités à distance](https://www.debian.org/doc/manuals/securing-debian-howto/ch-sec-tools.fr.html#s-vuln-asses)
- [Sécurité des appli web](https://blog.behrouze.com/securite/)


## Automatic security updates

To keep the computer with the latest security updates automatically
use package [UnattendedUpgrades](https://wiki.debian.org/UnattendedUpgrades)
with a [fix for raspbian buster](https://raspberrypi.stackexchange.com/a/102350)  
`sudo apt-get install unattended-upgrades`  
For mail support: `sudo apt-get install mailutils`

**Configuration**
Tutoriel : https://blog.behrouze.com/debian-auto-update-upgrade/

`/etc/apt/apt.conf.d/`

il faut au moins configurer 

* `50unattended-upgrades` ou `51unattended-upgrades-raspbian`  
* `20auto-upgrades`

Si on configure un fichier `51unattended-upgrades-raspbian` cela écrase les conf fichiers précédants dont `50unattended-upgrades`

Pour consulter sa configuration rapidement `sudo apt-config dump|grep Periodic`.  

**Executer l'update manuellement**
Pour vérifier ce qui sera installer `sudo unattended-upgrade -v -d --dry-run`.  
Pour exécuter la mise à jour `sudo unattended-upgrade -v`.

**Log** of last ugrades

`cat /var/log/unattended-upgrades`


