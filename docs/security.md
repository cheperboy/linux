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


## Configure firewall
see [tuto](https://www.tecmint.com/setup-ufw-firewall-on-ubuntu-and-debian/)

**Example: Chaudiere config**

allow ssh, samba, 5007tcp

**Usefull commands**

* `sudo apt-get install ufw` - Install
* `sudo ufw status numbered` - List rules 
* `sudo ufw enable` - Enable Firewall (may break ssh connection, allow ssh rule first)
* `sudo ufw disable` - Disable Firewall

**Enable by application name**

* `sudo ufw app list` - List applications
* `sudo ufw allow ssh` - Enable app ssh (on default port 22)

**Enable a specific port**

* `sudo ufw allow 2222/tcp` - Enable tcp ssh port 2222 

## SSH Key for github
see [tuto](https://help.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh)

**Check if keys already exist**  
`ls -al ~/.ssh`

**Generate key**  
`ssh-keygen -t rsa -b 4096 -C "my_email@mail.com"`  
When asked, save key to `/home/pi/.ssh/id_rsa`  
Add Public key (id_rsa.pub) to github account  
Test shell connection to github with `ssh -T git@github.com`. This will add github.com to the list of known hosts in `~/.ssh/known_hosts`  
