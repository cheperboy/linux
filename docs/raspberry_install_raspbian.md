# Raspbian Install & Configure

## Flash SD Card
1. Format SD card FAT32
2. Download [Raspbian](https://www.raspberrypi.org/downloads/raspbian/)
3. Flash image with [Etcher](https://www.balena.io/etcher/)
4. Create a file `boot/ssh` before booting raspbian to enable ssh

## Wifi setup before first boot
[help-1](https://www.raspberrypi.org/documentation/configuration/wireless/wireless-cli.md)
[help-2 !country not OK in this example!](https://howchoo.com/g/ndy1zte2yjn/how-to-set-up-wifi-on-your-raspberry-pi-without-ethernet)

Create file `boot/wpa_supplicant.conf`. (Raspbian will move it in `/etc/wpa_supplicant/` when the system is booted)

!!! warning
    EOL Conversion shall be **UNIX File Format**.

Add content:
``` bash
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=FR

network={
    ssid="YOUR_NETWORK_NAME"
    psk="YOUR_PASSWORD"
}
```

## Wifi setup after first boot
If conf is done after first boot, edit wpa_supplicant.conf  
`sudo nano /etc/wpa_supplicant/wpa_supplicant.conf`
```shell
network={
    ssid="YOUR_NETWORK_NAME"
    psk="YOUR_PASSWORD"
    key_mgmt=WPA-PSK
}
```

## Configuration
### Hostname and password
1.  Modify hostname, Edit `/etc/hostname` and `/etc/hosts`. Set to chaudiere (recognized on network as *chaudiere.local*)
2.  Modify pi password `sudo passwd pi`
 
### Package install
**Update/upgrade system and existing packages**

`sudo apt-get update` met à jour la liste des dépôts

`sudo apt-get dist-upgrade -y` met à jour tous les paquets installés vers les dernières versions en installant de nouveaux paquets si nécessaire

`sudo apt-get upgrade -y` met à jour tous les paquets installés sur le système

**Install packages**

`sudo apt-get -y install supervisor git python-pip nginx`

`pip install virtualenv virtualenvwrapper`
`mkvirtualenv whatever -p /usr/bin/python3`

[tuto-1](https://virtualenvwrapper.readthedocs.io/en/latest/install.html)
 | [tuto-2](https://medium.com/@ronm333/virtual-environments-on-the-raspberry-pi-ead158a72cd5)

**specific packages for chaudiere app**

`sudo apt-get install curl`

**clean**

`sudo apt-get clean` supprime les paquets téléchargés et stockés sur carte SD

