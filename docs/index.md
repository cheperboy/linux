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
`lsof file.txt` to see what processes are currently reading/writing the file  

**processus**  
`ps auxf` List all processes  
`kill -9 $(lsof -ti tcp:5007)` socket.error: [Errno 98] Address already in use. tue le processus serveur qui écoute le port 5007  
`killall -9 chromium-browse` Kill a process by name  
`sudo ss -ltnp` port listening (socket statistics)  
`sudo ss -ltnp | grep :port kill -9` port listening and killing zombie thread server  

**server / ports**  
`sudo ss -tulpn` Show servers and port listenning (socket statistics)  

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

**Mounts**  
`findmnt --fstab --evaluate` show fstab content with options
`mount` show devices currently mounted


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

#### NFS debug

After updating /etc/exports on server, run 

	exportfs -r

check if export is actually exported from server

	exportfs -av
	exportfs -sv
	showmount -e

from client

	showmount -e server_name # Check if server is providing some exports
	df 						 # Check if nfs export is actually mounted
	cat /etc/mtab | grep nfs # Show nfs currently mounted and nfs version used

#### NFS options

	no_root_squash

Problem: normal user can write but root cannot.
Explanation: NFS was designed with the idea that user and group ids would be the same on all machines across the network. For ordinary users, that works ok. But root's UID is always 0, and just because you have root on one box, it doesn't mean that you should have root access to every machine on the network.
Therefore, NFS treats root specially. By default, root is mapped to the nobody user, which normally has no write access. The no_root_squash option allows you to change how root is handled.
This option must be used for rsnapshot/rsync (to preserve ownership)


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
