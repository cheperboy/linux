## Install
- Kivy don't support python>3.7. Install python 3.7 (system wide) [using altinstall](https://hackersandslackers.com/multiple-versions-python-ubuntu/) to not mess the system python already installed.  

- Create a virtualenv using python3.7 `mkvirtualenv -p python3.7 venvname`  


- Install kivy pip package in the virtualenv
`pip install kivy`  
`pip install kivy_examples`  
Check kivy linux installation [doc](https://kivy.org/doc/stable/installation/installation-linux.html) if needed

- Modify ~/.kivy/config.ini
``` ini
[graphics]
fullscreen = 0
multisamples = 0
rotation = 0

[input]
mouse = mouse
```

