## Supervisorctl custom alias functions
function start { sudo supervisorctl start "$@" ; }
function restart { sudo supervisorctl restart "$@" ; }
function stop { sudo supervisorctl stop "$@" ; }

## alias ls
alias ls='ls --color=auto --group-directories-first'
alias l='ls -lAh'
alias ll='ls -CFAh'
alias la='ls -CFAh'
alias lr='ls -lARh' ## list recursively

## cd to a dir and list all files 
function cd { builtin cd "$@" && l ; }
alias ..='cd ..'

## nginx
alias nginx_status='sudo service nginx status'
alias nginx_start='sudo service nginx start'
alias nginx_restart='sudo service nginx restart'
alias nginx_stop='sudo service nginx stop'

## supervisor
alias status='sudo supervisorctl status'
alias reread='sudo supervisorctl reread'
alias reload='sudo supervisorctl reload'
alias start_all='sudo supervisorctl start all'
alias stop_all='sudo supervisorctl stop all'

## python
alias python=python3
alias pip=pip3

## aliases others
alias top='htop'
alias tail='colortail'

export PATH=$PATH:/home/pi/.local/bin
## load virtualenvwrapper for python (after custom PATHs)
export WORKON_HOME=~/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
source /home/pi/.local/bin/virtualenvwrapper.sh

## Usefull commands
# lsblk        # list devices with mount points
# tree         # Tree representation
# tree -d      # Tree representation, directories only

# Alias for dev alarm
alias log='cd /home/pi/Prod/home_alarm_LOG'
alias prod='cd /home/pi/Prod/'
alias dev='cd /home/pi/Dev/home_alarm/src'
alias deploy='/home/pi/.virtualenvs/prod/bin/python /home/pi/Dev/home_alarm/src/installer.py deploy-from-dev'
alias bashrc='nano ~/.bashrc'

dev
workon dev
