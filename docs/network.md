## CIDR adress range notation
192.168.1.0/24 adress range 192.168.1.0 - 192.168.1.255

## Local DNS
The DNS of a linux machine is configure in `etc/hosts`.  
Adding `192.168.1.50 nas-home` in this file, the machine will replace this name with the ip (anytime this name is used in a network service like ping, nfs share, etc).

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

###Host scanner

	nmap -v -A 192.168.1.52
