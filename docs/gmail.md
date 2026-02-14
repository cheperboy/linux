# Gmail

## Gmvault
Savegarde gmail.

### Installation Gmvault
Require python2.7

    mkvirtualenv -p python2.7 gmvault
    pip install gmvault

### Creation compte email pour backup
elisjo2@gmail

Autoriser les applications à se connecter au compte gmail

    Gmail account settings -> Less secure app access -> Authorize

### Copie local des emails
    gmvault sync elisjo@gmail.com -p

### Restaurer la copie local vers le compte secondaire

    gmvault restore -d ~/gmvault-db elisjo2@gmail.com -p
    
