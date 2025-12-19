## network commands

### liste des interface et leur configuration

`ip addr`

### socket stat

`sudo ss -nltu`  
`sudo ss -antpl` (processus)  

### arp    
display or modify ARP cache information. The ARP cache is simply a table that provides a mapping of IP addresses to their MAC addresses in the network.  
`arp`  

### nmcli

`nmcli`  
`nmcli device show eno1`  
`nmcli connection show` show status of all interfaces  

### iftop / bmon

monitoring bandwidth usage on a specific network interface.  
`sudo iftop`  
`bmon`  


## Réseau IP v4
## CIDR adress range notation
192.168.1.0/24 adress range 192.168.1.0 - 192.168.1.255 (/24 correspond ua masque 255.255.255.0).  

## Local DNS
The DNS of a linux machine is configure in `etc/hosts`.  
Adding `192.168.1.50 nas-home` in this file, the machine will replace this name with the ip (anytime this name is used in a network service like ping, nfs share, etc).

### Adresse IP (ré.se.au.machine) 
https://openclassrooms.com/fr/courses/6944606-concevez-votre-reseau-tcp-ip/7236450-identifiez-votre-machine-au-sein-de-plusieurs-reseaux  

Une adresse est constituée de 4 paquets de 8 bits. une partie de l'adresse définit le réseau et l'autre partie la machine. le masque indique combien de bits définissent le réseau.
192.168.1.1/24 signifie que les 24 premiers bits définissent le **nom du réseau** (192.168.1.x) et les 8 derniers le nom de la machine (x.x.x.1).  
Analogie: nom du réseau = nom de la rue. nom de la machine = numéro de la maison.  
L'adresse d'un réseau s'obtient en prenant l'adresse d'une machine appartenant à ce réseau et en remplaçant les bit de la machine par 0 -> le nom du réseau est 192.168.1.0.  

    adresse             adresse du réseau   adresse de la machine   masque
    192.168.1.1/24      192.168.1.0         x.x.x.1                 255.255.255.0
    192.168.1.1/16      192.168.0.0         x.x.1.1                 255.255.0.0
    192.168.1.1/8       192.0.0.0           x.168.1.1               255.0.0.0

Deux machines ne peuvent communiquer que si elles sont sur le même réseau.  
Pour faire communiquer deux macine qui sont sur des réseaux différents il faut qu'un routeur s'interface entre les deux réseaux et qu'on lui configure une fonction de passerelle.  


### Table de routage IP du noyau
`route -n`

    Destination     Passerelle      Genmask         Indic Metric Ref    Use Iface
    0.0.0.0         192.168.1.254   0.0.0.0         UG    100    0        0 eno1
    192.168.1.0     0.0.0.0         255.255.255.0   U     100    0        0 eno1

La destination (Réseau) : adresse IP qui indique quels sont les paquets de données qui vont suivre cette route selon leur destination.  
La passerelle (Gateway) : c'est une adresse IP qui indique par où les paquets vont passer pour arriver à destination. Ils seront envoyés à cette adresse.  
Le masque de sous-réseau (Genmask) : c'est une suite de 4 octets (comme une adresse IP) qui permet d'indiquer quelle est la taille de chaque partie de l'adresse IP (partie réseau et partie hôte).  
- ligne 2: tous les paquets à destination du réseau 192.168.1.0 ( = le réseau local) sont envoyé **directement** à l'adresse de destination, sans passer par une passerelle.  
- ligne 1: tous les paquets à destination du réseau 0.0.0.0 (= n'importe quel réseau autre que le réseau local) seront envoyés à l'adresse 192.168.1.254 ( = le routeur du réseau local) qui est la passerelle vers les autres réseaux.

### réseau de machine sans routeur
Pour que les machines communiquent, leur affecter des adresses de sorte qu'elles soient sur le même réseau.  
par exemple 192.168.1.1/24 et 192.168.1.2/24  
idem si machines reliées par un switch.  

Pour qu'une machine (sans configuraiton réseau) connectée au switch puisse communiquer avec les autres, l'une des machine doit exécuter un serveur DHCP afin de fournir une adresse à la nouvelle machine. 

## Share NFS directory from Raspbian server
Install ressource

	sudo apt-get update
	sudo apt-get install nfs-kernel-server nfs-common

Configurer l'export: `sudo nano /etc/exports`
	
	/home/pi/Dev asus.local(rw,all_squash,anonuid=1000,anongid=1000,sync)

On peut utiliser des ranges d'adresse ip ou wilcards pour partager sur plusieurs machine `192.168.1.*`

Redémarrer le service

	sudo service nfs-kernel-server restart

## Mount NFS share from Raspbian server to linux client
Install ressource
	sudo apt-get update
	sudo apt-get install nfs-common

Vérifier que les deux services nécessaires sont actifs (rpcbind et nfs-common).

	sudo service rpcbind status
	sudo service nfs-common status

Créer le point de montage et le rendre accessible au user cheperboy (ou pi)

	sudo mkdir /media/alarm_dev
	sudo chown cheperboy /media/alarm_dev

Commande pour monter le disque

	sudo mount -t nfs alarm.local:/home/pi/Dev /media/alarm_dev

Edit fstab pour monter au démarrage `sudo nano /etc/fstab`

	alarm.local:/home/pi/Dev /media/alarm_dev nfs defaults, netdev,rw 0 0


## Mount distant NAS NFS directory on linux
Edit distant nas shared folder, add nfs share.

Create local mount point 
	
	sudo mkdir /media/backup

Edit fstab
	
	192.168.1.52:/volume1/backup/ /media/NAS_ORS/backup nfs defaults,user,auto,noatime,bg,nfsvers=3 0 0

Mount and give permission
 
	mount -a
	sudo chmod 777 /media/backup

## Mount Synology SMB share (no fstab)
sudo mkdir /mnt/nas
sudo mount -t cifs -o username=myname,uid=myname,gid=myname //nasmlv.local/homes/myname /mnt/nas

## Nmap

### LAN scanner

simple

	nmap -sP -O 192.168.1.0/24

full

	sudo nmap -sT -O 192.168.1.0/24

hostname (not working)
	
	nmap -sL 192.168.1.0/24

### Host scanner

	nmap -v -A 192.168.1.52

### Host vulnerability

Update scripts before vuln scan

    sudo nmap --script-updatedb

scan host for vulnerability

    sudo nmap -Pn --script vuln <HOST>

