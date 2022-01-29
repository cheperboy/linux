## General links
- [raspberry.org - basic security](https://www.raspberrypi.org/documentation/configuration/security.md)
- [pestmeester.nl - complete guide including ssl certificate and ssh-keygen](http://pestmeester.nl/)
- [debian.org - securing-debian-howto](https://www.debian.org/doc/manuals/securing-debian-howto/ch-sec-services.fr.html)
- [debian.org - evaluation des vulnérabilités à distance](https://www.debian.org/doc/manuals/securing-debian-howto/ch-sec-tools.fr.html#s-vuln-asses)
- [Sécurité des appli web](https://blog.behrouze.com/securite/)


## Debian Automatic security updates

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
### Create public key
see [tuto](https://help.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh)

**Check if keys already exist**  
`ls -al ~/.ssh`

**Generate key**  
`ssh-keygen -t rsa -b 4096 -C "my_email@mail.com"`  
When asked, save key to `/home/pi/.ssh/id_rsa`  
Add Public key (id_rsa.pub) to github account  
Test shell connection to github with `ssh -T git@github.com`. This will add github.com to the list of known hosts in `~/.ssh/known_hosts`  

**Add SSH key to the ssh-agent**  
Start the ssh-agent in the background.  
`eval "$(ssh-agent -s)"`

Add SSH private key to the ssh-agent. If created key with a different name, replace `id_rsa` in the command with the name of your private key file.  
`ssh-add ~/.ssh/id_rsa`

Useful commands:  
To delete all cached keys before `ssh-add -D`  
To check your saved keys `ssh-add -l`  

### Modify ssh config
`nano cd ~/.ssh/config`  

	# Github cheper account
		Host github.com
		HostName github.com
		User git
		IdentityFile ~/.ssh/id_rsa
		IdentitiesOnly yes

`IdentitiesOnly yes` may be required if multiple id_rsa files exists on the system. This option will prevent the SSH default behavior of sending the identity file matching the default filename for each protocol. If you have a file named ~/.ssh/id_rsa that will get tried BEFORE your ~/.ssh/id_rsa.github without this option.  

### Modify Git config  
`git config --global user.name "cheper"`  
`git config --global user.email "my_email@gmail.com"`  

Inside the local directory of the git repo named 'linux'  
`git remote set-url origin git@github.com:cheper/linux.git`  
This will update the file .git/config to use ssh protocol instead of https.  

# GnuPG

Install `sudo apt install gnupg`
`-a --armor`		ASCI output (can be sent via email)  
`-c --symmetric`	Encrypt with simple password (symmetric, no public/private key)  
`-d --decrypt`		Decrypt  
`-o --output`		file output instead of stdout/console  
`--no-symkey-cache` Ne pas conserver le mot de passe pendant la session

# Encrypt (symmetric)

`gpg -c -a file.txt`
`gpg --symmetric --armor file.txt`

# Decrypt

`gpg -d file.txt.gpg` output to console
`gpg -o file.txt -d file.txt.gpg` output to a file
`cat file.txt.gpg | gpg -d`

# Gedit shortcut

`Ctrl + Maj + E` Encrypt (symmetric)
`Ctrl + Maj + D` Decrypt

