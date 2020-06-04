####################################
# filename ~/.cheperboy_profile.sh #
####################################

# Add the following in ~/.zshrc
# if [ -f ~/cheperboy_profile.sh ]; then
#     . ~/cheperboy_profile.sh
# fi


#########
# Alias #
#########

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

## alias cat
alias cat="highlight -O ansi --force"
alias bcat="highlight -O ansi --syntax=bash"

## to execute "history | grep foo" just enter "history foo"
function history {
  if [[ $# -eq 0 ]] ; then # (if no parameter given)
    builtin history
  else
    builtin history | grep "$@"
  fi
}

## cd to a dir and list all files
function cd { builtin cd "$@" && l ; }
# alias ..='cd ..' # useless with zsh

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

#########################
# Virtualwrapper loader #
#########################
export PATH=$PATH:/home/pi/.local/bin
# load virtualenvwrapper for python (after custom PATHs)
export WORKON_HOME=~/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
source /home/pi/.local/bin/virtualenvwrapper.sh

#############################
# Reminder Usefull commands #
#############################
# lsblk        # list devices with mount points
# tree         # Tree representation
# tree -d      # Tree representation, directories only

####################################
# Alias for dev home_alarm project #
####################################
alias log='cd /home/pi/Prod/home_alarm_LOG'
alias prod='cd /home/pi/Prod/'
alias dev='cd /home/pi/Dev/home_alarm/src'
alias deploy='/home/pi/.virtualenvs/prod/bin/python /home/pi/Dev/home_alarm/src/installer.py deploy-from-dev'
alias bashrc='nano ~/.bashrc'


####################
# Prompt with venv #
####################
function virtualenv_info {
    # Get Virtual Env
    if [[ -n "$VIRTUAL_ENV" ]]; then
        # Strip out the path and just leave the env name
        echo "(${VIRTUAL_ENV##*/}) "
    fi
}
# disable the default virtualenv prompt change
export VIRTUAL_ENV_DISABLE_PROMPT=1

VENV="\$(virtualenv_info)";
# Add color to venv string
VENV="%F{green}${VENV}%f"

# simple prompt like "cwd %"
PROMPT="%F{blue}%~ %f%# "
# prepend "user@host"
PROMPT="%F{white}$USER%f@%F{white}%m ${PROMPT}"
# prepend "(venv)"
PROMPT="${VENV}${PROMPT}"

########################
# Commands after login #
########################

# uptime information and who is logged in
w

################################
# Custom  commands after login #
################################
# Load virtual dev
workon dev

# goto dir /home/pi/Dev/home_alarm
dev

