# .bashrc

``` bash
# cd to a dir and list all files 
function cs {
	builtin cd "$@" && ls -F
}

# aliases directories
alias ..='cd ..'
alias ls='ls -CF'
alias la='ls -la'
alias lr='ls -Rh' # list recursively

# python
alias python=python3
alias pip=pip3

# aliases others
alias top='htop'

# other alias
alias dev='cd /home/pi/Dev/'
alias prod='cd /home/pi/Prod/'

# load virtualenvwrapper for python (after custom PATHs)
# export WORKON_HOME=~/Envs
# export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
# source /home/pi/.local/bin/virtualenvwrapper.sh

# Usefull commands
# lsblk     	#list devices with mount points
```


# File Sharing
## NFS

https://help.ubuntu.com/community/SettingUpNFSHowTo

### Mount NFS drive (synology) from linux (NFSV4 client)

``` bash
sudo mkdir /media/nas
sudo mount -t nfs -o proto=tcp,port=2049 192.168.1.52:/volume1/hpsrv-backup /media/nas
sudo chmod xxx /media/nas
```

To do this on startup, edit /etc/fstab:
``` bash
<nfs-server-IP>:/   /mnt   nfs    auto  0  0
```

## Samba
[turn-your-raspberry-pi-into-a-nas-box/](https://www.makeuseof.com/tag/turn-your-raspberry-pi-into-a-nas-box/)

# Backup
## rsync (synchronize / mirror)
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
- [raspberry](https://www.vdsar.net/rsync-backup-synology-remote-raspberry-pi/)  
- [synology](https://www.synology.com/en-global/knowledgebase/DSM/tutorial/Backup_Restore/How_to_back_up_Linux_computer_to_Synology_NAS)


# Administration

## ssh

## webmin

installation (ubuntu 18)

``` bash
sudo sh -c 'echo "deb http://download.webmin.com/download/repository sarge contrib" > /etc/apt/sources.list.d/webmin.list'
wget -qO - http://www.webmin.com/jcameron-key.asc | sudo apt-key add -
sudo apt-get update
sudo apt-get install webmin
sudo ufw allow 10000/tcp
```
[https://localhost:10000](https://localhost:10000)

# Security

## Firewall (UFW)

>	/!\ Do not enable if webmin is active on the system  	

`sudo ufw status verbose`

https://www.tecmint.com/setup-ufw-firewall-on-ubuntu-and-debian/
```
## fail2ban
`sudo apt-get install fail2ban`

# Log
`journalctl -u motioneye > motioneye.log` Export log to a file  
`journalctl -n 20` Show last 20 lines of system log  
`journalctl -f` show live log  
