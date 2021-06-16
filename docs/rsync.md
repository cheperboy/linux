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


