## Usefull Commands

**Interfaces**  
`lsusb`  Liste les périphériques USB  
`dmesg | grep tty` Trouver le nom du périphérique série qui vient d’être branché  
`lsblk` List devices with mount points  
`sudo iw wlan0 scan` Scan available wifi networks  

**Files**  
`sudo chown pi mydb.db` Le propriétaire du fichier mydb.db devient l’utilisateur “pi”  
`chmod a+x run.py` rend le fichier exécutable (change les permissions)  
`stat -c "%a %n" file.txt` to see file permission in octal (777..)  

**processus**  
`ps auxf` List all processes  
`kill -9 $(lsof -ti tcp:5007)` socket.error: [Errno 98] Address already in use. tue le processus serveur qui écoute le port 5007  
`killall -9 chromium-browse` Kill a process by name  
`sudo netstat -ltnp` port listening  
`sudo netstat -ltnp | grep :port kill -9` port listening and killing zombie thread server  

**server / ports**  
`sudo netstat -tulpn` Show servers and port listenning  

**disk usage**  
Trier par taille, plus grand en premier:  
`sudo du -shc /var/* | sort -rh` dossiers  
`ls -lh --sort=size` fichiers  
`du -kx | egrep -v "\./.+/" | sort -nr` fichiers et dossiers  

`du -xksh ./* | sort -n` Espace utilisé  
`du -hs`  
`df -h`  
`cat /proc/meminfo` : affiche l’état d’utilisation de la mémoire  

**Partitions**  
`lsblk` liste les partitions (attention: ne montre pas l'ordre réelle sur le disque)  
`blkid` UUID des partitions  
`sudo fdisk -l` liste les partitions (avec secteurs de début/fin)  

**copy / moove**  
`cp -r source/ dest/` copie le répertoir “source” et son contenu dans le répertoire “dest”. résultat: il existe un chemin `dest/source/file.txt`  
`cp -p fstab fstab.old` copie de sauvegarde conservant les permissions/mode/propriétaire  
`mv foo/ bar/` Déplace le répertoir `foo` et son contenu dans le répertoire `bar`. résultat: il existe un chemin `bar/foo/file.txt`  
`mv foo bar` Renomme le répertoir ou le fichier `foo` en `bar`  
`rm -r dir/` supprime le répertoire `dir` et son contenu  

**console**  
`tree` Tree representation  
`tree -d` Tree representation, directories only  

**commandes d'administration**  
supprimer les snaps inutiles
`snap list --all | awk '/désactivé|disabled/{print $1, $3}' | while read snapname revision; do sudo snap remove "$snapname" --revision="$revision"; done`  



## Files permissions
	User, Group, Others
	0 No permission 
	1 Execute permission 
	2 Write permission 
	3 Execute and write permission: 1 (execute) + 2 (write) = 3 
	4 Read permission 
	5 Read and execute permission: 4 (read) + 1 (execute) = 5 
	6 Read and write permission: 4 (read) + 2 (write) = 6 
	7 All permissions: 4 (read) + 2 (write) + 1 (execute) = 7

**default permission**  
	files 644  
	directory 755 (execute means ability to cd into the directory)

To change all the directories to 755 (drwxr-xr-x):  
`find /opt/lampp/htdocs -type d -exec chmod 755 {} \;`  
To change all the files to 644 (-rw-r--r--):  
`find /opt/lampp/htdocs -type f -exec chmod 644 {} \;`  



## File Sharing
### NFS

https://help.ubuntu.com/community/SettingUpNFSHowTo

#### Mount NFS drive (synology) from linux (NFSV4 client)

``` bash
sudo mkdir /media/nas
sudo mount -t nfs -o proto=tcp,port=2049 192.168.1.52:/volume1/hpsrv-backup /media/nas
sudo chmod xxx /media/nas
```

To do this on startup, edit /etc/fstab:
``` bash
<nfs-server-IP>:/   /mnt   nfs    auto  0  0
```

### Samba
[turn-your-raspberry-pi-into-a-nas-box/](https://www.makeuseof.com/tag/turn-your-raspberry-pi-into-a-nas-box/)  
[share a directory](http://www.framboise314.fr/partager-un-repertoire-sous-jessie-avec-samba/)

`sudo apt-get install samba samba-common-bin`  
`sudo nano /etc/samba/smb.conf`  

**Guest account (no password)**
To add at the end of smb.conf :  
``` bash
[public]
comment = Partage Samba sur Raspberry Pi
path = /home/pi/partage
writable = yes
guest ok = yes
guest only = yes
;create mode = 0777
;directory mode = 0777
share modes = yes
force user = pi
force group = pi
```

**Private account**

Create user 'pi' with the following command:
`sudo smbpasswd -a pi`

``` bash
[private]
comment = Dev_chaudiere
path = /home/pi/private
writable = yes
create mode = 0777
directory mode = 0777
public = no
```

Restart service  
`sudo systemctl restart smbd.service`

From Windows PC  
`\\server_ip\samba_share_name`



## Backup
### Rsnapshot

	rsnapshot configtest
	rsnapshot du
	rsnapshot hourly

sauvegarde distante du dernier snapshot
	
	rsync -avh --delete --progress dest/hourly.0/ distant_backup/
	ajouter -x pour compresser le transfert. supprimer --progress si pas en console.
	

### rsync (synchronize / mirror)
Synchronize datas from media 1 to media 2
``` bash
sudo apt-get install rsync
rsync -av --delete /media/1/shares /media/2/shares/
```

Run this command every day at 5h00
``` bash
crontab -e
30 5 * * * rsync -av --delete /media/1/shares /media/2/shares/
```

tuto :  
- [raspberry to synology](https://www.vdsar.net/rsync-backup-synology-remote-raspberry-pi/)  
- [synology.com](https://www.synology.com/en-global/knowledgebase/DSM/tutorial/Backup_Restore/How_to_back_up_Linux_computer_to_Synology_NAS)



## Administration

### ssh

*Configure ssh keys*  

* https://kb.iu.edu/d/aews
* https://www.cyberciti.biz/faq/how-to-set-up-ssh-keys-on-linux-unix/
* https://nerderati.com/2011/03/17/simplify-your-life-with-an-ssh-config-file/
	
### webmin

installation (ubuntu 18)

``` bash
sudo sh -c 'echo "deb http://download.webmin.com/download/repository sarge contrib" > /etc/apt/sources.list.d/webmin.list'
wget -qO - http://www.webmin.com/jcameron-key.asc | sudo apt-key add -
sudo apt-get update
sudo apt-get install webmin
sudo ufw allow 10000/tcp
```
[https://localhost:10000](https://localhost:10000)

## Security

### Firewall (UFW)

!!! Warning "Do not enable if webmin is active on the system"

`sudo ufw status verbose`

https://www.tecmint.com/setup-ufw-firewall-on-ubuntu-and-debian/

### fail2ban
`sudo apt-get install fail2ban`

## Log
**main log files**  

* `/var/log/syslog` - main log file for all services
* `/var/log/message` - whole systems log file
* `/var/log/auth.log` - all authentication attempts are logged here

**usefull commands**  

* `journalctl -u motioneye > motioneye.log` Export log to a file  
* `journalctl -n 20` Show last 20 lines of system log  
* `journalctl -f` show live log  
* `tail -f my_log_file.log` show live log of custom file  
* `tail -f log/*` show live log of all files in log/ directory  
