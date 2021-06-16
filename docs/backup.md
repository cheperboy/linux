# Backup

## softwares

`BackInTime` Sauvegarde de donénes    
`timeshift` Sauvegarde du système et fichiersde conf système

- rdiff-backup: incremental, the last backup contains the diff compared to the previous one and so on. if a run failed (network issue) then all following backups are irrelevant. 
- rsnapshot: Based on rsync. Designed to pull backup from a server. So it is good from server to server. pushing to nfs works but is not the intended use of this program. what is the behaviour in case of interrupted backup? use hard links to store only diff. the most recent backup is a mirror of the source dir. older backup dirs are hard links to this miror or files modified. 
- rsync: not impacted in case of network failure, the next run will update the missing files. --backup option can save the diffs compared to previous run, althouth it does not tell is the file is modified or deleted. with a dedicated script, rsync can provide a mirror + some info about what file was modified when. 

### Rsnapshot

	rsnapshot configtest
	rsnapshot du
	rsnapshot hourly

sauvegarde distante du dernier snapshot
	
	rsync -avh --delete --progress dest/hourly.0/ distant_backup/
	ajouter -x pour compresser le transfert. supprimer --progress si pas en console.

# Exemple config rsnapshot overs NFS
from client *asus.local* /home/cheperboy/poubelle/source/ 
to server *debhp* /media/dd1t/backup_asus/test

server side, setup nfs share: edit `/etc/exports`
	
	/media/dd1t/backup_asus asus.local(rw,sync,no_root_squash)

client side, mount nfs share: edit `/etc/fstab` then `sudo mount -a`

	debhp:/media/dd1t/backup_asus /media/debhp/backup_asus nfs defaults 0 0

Client side, edit /etc/rsnapshot_debhp.conf.conf

	config_version	1.2
	snapshot_root	/media/debhp/backup_asus/root
	no_create_root	1
	cmd_cp		/bin/cp
	cmd_rm		/bin/rm
	cmd_rsync	/usr/bin/rsync
	cmd_logger	/usr/bin/logger
	retain	hourly	6
	retain	daily	7
	retain	weekly	4
	retain	monthly	2
	verbose		4
	loglevel	3
	logfile	/var/log/rsnapshot.log
	lockfile	/var/run/rsnapshot.pid
	link_dest	1
	backup	/home/cheperboy/poubelle/source/	test/

Create the snapshot_root directory.note that when the nfs share is not mounted, this directory won't be created thanks to no_create_root 1. This avoid filling the cliet disk.

	mkdir -r /media/debhp/backup_asus/root

run 

	sudo rsnapshot -c rsnapshot_debhp.conf.conf hourly

Check

	sudo rsnapshot -c rsnapshot_debhp.conf.conf du


### rsync (synchronize / mirror)

#### rsync basics

*Files permissions and ownership*  
In order to preserve permissions, rsync must bu run as root. Indeed, as a normal user you can't create files that don't belong to you, so you need to either log in as root on the destination, or you have to be root locally and run rsync in the opposite direction and pull the files in.  

By default rsync will try to match the ownership by username / groupname. In other words when the user *toto* is the owner of a file at the source, rsync will make the user *toto* also the owner at the destination (even when they have different UID/GID numbers).  
That is usually quite resilient and the most predictable for humans as we normally don't look at ownership in the form of UID/GID numbers.  

When no matching user *toto* is present on the remote destination, then a fall-back scenario will happen. Rsync will then preserve the actual underlying UID/GID numbers of the *toto* user on the source will used to set the owner.  

That should preserver the correct ownership when you reverse the rsync direction and restore the backup.  

If the option *--numeric-ids* is used, rsync don't try to match username / groupname of the source / destination and the numeric ID from the source system is used.  

#### sync
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



## Rsync

rules
- always use sudo to call rsync (to grant ability to check/modify ownership/permissions)
- mind the */* at the end of the path (dir of files inside the dir)


# backup
    
sudo rsync -avh --progress --delete /home/cheperboy/poubelle/source/ /media/debhp/backup_asus/rsync

# diff
sudo rsync -ani --delete /home/cheperboy/poubelle/source/ /media/debhp/backup_asus/rsync

# restore
sudo rsync -avh --delete /media/debhp/backup_asus/rsync/ /home/cheperboy/poubelle/source



# restore snapshot

sudo rsync -avh --delete /media/debhp/backup_asus/root/hourly.0/test/home/cheperboy/poubelle/source/ /home/cheperboy/poubelle/rsnapshot_restore


