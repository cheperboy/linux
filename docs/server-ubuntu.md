# Ubuntu server install

## Configuration mail sender MTA postfix
[digitalocean - how-to-install-and-configure-postfix-as-a-send-only-smtp-server-on-ubuntu-22-04](https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-postfix-as-a-send-only-smtp-server-on-ubuntu-22-04)

Prérequis:

 - mondomaine.fr doit être un FQDN.
 - Le domaine doit avoir un DNS record A pointant vers l'adresse ip publique.

### config

* sudo nano /etc/mailname

`mondomaine.fr`

* sudo nano /etc/postfix/main.cf  
```
**myhostname = mondomaine.fr**
alias_maps = hash:/etc/aliases
alias_database = hash:/etc/aliases
mydestination = $myhostname, localhost.$mydomain, localhost, $mydomain
relayhost =
mynetworks = 127.0.0.0/8
mailbox_size_limit = 0
recipient_delimiter = +
**inet_interfaces = loopback-only**
inet_protocols = ipv4
myorigin = /etc/mailname
```

`sudo systemctl restart postfix`

test with :

    echo "body of the email" | mail -s "subject" someone@email.com


* forward system mails

sudo nano `/etc/aliases`. Add the following line to the end of the file:  

    root:          your_email_address

Apply and restart Postfix:

    sudo newaliases
    sudo systemctl restart postfix

Test with :

    echo "body of the email" | mail -s "subject" root

## App install

### Docker compose

[tutorial](https://docs.docker.com/engine/install/ubuntu/)  

`sudo apt install docker-compose`

### python3

venv in `~/pyenv`  
installation : `sudo apt install python3-venv`  
create a virtual env:  
```
cd
python3 -m venv pyenv
```
Activate :
```
source ~/pyenv/bin/activate
pip install some-package
```




## Basic security tips

### Hardening tips
* [https://askubuntu.com/questions/151440/important-things-to-do-after-installing-ubuntu-server](https://askubuntu.com/questions/151440/important-things-to-do-after-installing-ubuntu-server)

### usefull service to install
`gedit python3-virtualenv curl whois nmap htop python3-virtualenv nmap fail2ban avahi-utils ssh unattended-upgrades mailutils inetutils-traceroute certbot`


### Disable root user:

`sudo passwd -l root`

### Configure sshd

Disable ssh some options in `/etc/ssh/sshd_config` then restart ssh with the command `/etc/init.d/ssh restart`  

```sh
PermitRootLogin no
PermitEmptyPasswords no
```

### Configure firewall

``` Shell
sudo ufw status
sudo ufw allow ssh
sudo ufw allow http
or
sudo ufw allow 80/tcp
sudo ufw enable
```

### install fail2ban

    sudo apt-get install fail2ban

### rootkit

`sudo apt-get install rkhunter chkrootkit`

``` sh
sudo rkhunter --update
sudo rkhunter --propupd
sudo rkhunter --check
```
