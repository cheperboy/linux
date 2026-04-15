# Install Debian 13 (trixie)

## Disable root account

**Add normal user to sudo**  
Le mieux est de ne pas définir de mot de passe root lors de l'installation. Cela ajoute automatiquement l'utilisateur au groupe sudo.  
Sinon après l'installation :  
```sh
su  # log as root
apt update && apt install sudo # Installer la commande sudo
adduser $MY_SUBUSER sudo # Ajouter l'utilisateur au groupe sudo (chemin /usr/sbin/adduser). ou bien utiliser la commande `usermod –aG sudo $MY_USER`
su $MY_SUBUSER # log back to normal user. # se loger avec l'utilisateur
```

**Disable root login**  
```sudo nano /etc/passwd```
replace the shell path `/bin/bash` (or similar) with `/sbin/nologin`:
`root:x:0:0:root:/root:/sbin/nologin`

## Install nala and usefull apps
```sh
sudo apt install nala
```

- minimal: `gedit python3-venv curl htop fail2ban ssh nmap unattended-upgrades highlight`
- more: `whois nmap htop avahi-utils mailutils inetutils-traceroute certbot`

## Gnome extension

https://extensions.gnome.org/extension/307/dash-to-dock/

## install docker 

https://docs.docker.com/engine/install/debian/
https://docs.docker.com/engine/install/linux-postinstall/

1. Set up Docker's apt repository.

```sh
# Add Docker's official GPG key:
sudo apt update
sudo apt install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
sudo tee /etc/apt/sources.list.d/docker.sources <<EOF
Types: deb
URIs: https://download.docker.com/linux/debian
Suites: $(. /etc/os-release && echo "$VERSION_CODENAME")
Components: stable
Architectures: $(dpkg --print-architecture)
Signed-By: /etc/apt/keyrings/docker.asc
EOF

sudo nala update
```

2. Install the Docker packages.

```
sudo nala install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
# Check running correctly
sudo systemctl status docker
sudo docker run hello-world
```

3. post install

The docker group grants root-level privileges to the user. 

```
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker
```


### Docker monitoring ctop

https://github.com/bcicen/ctop?tab=readme-ov-file

```
sudo nala install ca-certificates curl gnupg lsb-release
curl -fsSL https://azlux.fr/repo.gpg.key | sudo gpg --dearmor -o /usr/share/keyrings/azlux-archive-keyring.gpg
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/azlux-archive-keyring.gpg] http://packages.azlux.fr/debian \
  $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/azlux.list >/dev/null
sudo nala update
sudo nala install docker-ctop
```




