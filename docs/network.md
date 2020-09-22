## CIDR adress range notation
192.168.1.0/24 adress range 192.168.1.0 - 192.168.1.255

# Mount distant NAS NFS directory on linux
Edit distant nas shared folder, add nfs share.

Create local mount point 
	sudo mkdir /media/backup

Edit fstab
	192.168.1.52:/volume1/backup/ /media/NAS_ORS/backup nfs defaults,user,auto,noatime,bg,nfsvers=3 0 0

	mount -a
	sudo chmod 777 /media/backup
