## Git

[interractive commands](https://ndpsoftware.com/git-cheatsheet.html#loc=index;)

**global conf stored in ~/.gitconfig**  

    git config --help

**Create from existing data**  

    cd my_project_dir
    git init
    git add .
    
**Create from existing repository**  
    
    git clone

**Show**  
    
    git status
    git diff
    
**Update**  
Fetch latests changes from origin, does not merge
    
    git fetch
    
Pull latest changes from origin and merge
    
    git pull

**Publish**

    git commit -am "message"
    git push
	
## Colortail

like tail with color

	sudo apt-get install colortail
	colortail -f myapp.log
	
sample conf for log to add in colortail.conf

	nano /etc/colortail/colortail.conf


``` sh
# matches the word FOO
# ^.*(FOO).*$

COLOR brightred
{
^.*(CRITICAL).*$
^.*(ERROR).*$
}
COLOR yellow
{
^.*(WARNING).*$
}
COLOR green
{
^.*(INFO).*$
}

```

## Putty

* [Themes](https://www.noobunbox.net/themes-pour-putty/theme-glacier-remix)
* [MTPutty](https://ttyplus.com/multi-tabbed-putty/)
 
## Python

* [color log](https://medium.com/@galea/python-logging-example-with-color-formatting-file-handlers-6ee21d363184)
 
### Import beyond top level package

``` python
import sys
from os.path import abspath as abspath
from os.path import dirname as dirname
from os.path import basename as basename
from os.path import join    as join

module_path  = abspath(dirname(__file__)) # /home/pi/Dev/home_alarm/src/nox_alarm
src_path     = dirname(module_path)       # /home/pi/Dev/home_alarm/src
sys.path.append(src_path)
```

### SQLAlchemy

* [filters (like, or, in, ...)](http://www.leeladharan.com/sqlalchemy-query-with-or-and-like-common-filters)

### Mkdocs

	mkdocs serve --dev-addr 0.0.0.0:8001


