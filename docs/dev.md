# Dev tools

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
 
## Mkdocs

	mkdocs serve --dev-addr 0.0.0.0:8001


## Sublime
**shortcuts** 
* `ctrl + R` show function list
* `ctrl + L` select line
* `ctrl + maj + K` delete line
* `ctrl + shift + up` move line up

* `ctrl + P` show interactive menu
