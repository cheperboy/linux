# on most systems, .bashrc already contains 'source .bash_aliases'

alias ..="cd .."
alias lsblk="lsblk -a -o NAME,LABEL,MOUNTPOINT,SIZE,FSUSE%,MODEL,UUID"
# xclip to copy file content to clipboard. require : sudo apt install xclip
alias cpc="xclip -sel c < " # use it like this: cpc file_name
alias myip="ip addr show eno1 | grep inet | awk '{ print $2; }' | sed 's/\/.*$//'"
alias ccat="highlight -O ansi --force"
alias bcat="highlight -O ansi --syntax=bash"
