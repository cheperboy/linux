alias ..='cd ..'
alias lsblk=lsblk -a -o NAME,LABEL,MOUNTPOINT,SIZE,FSUSE%,MODEL,UUID
# xclip to copy file content to clipboard. require : sudo apt install xclip
alias cpc="xclip -sel c < " # use it like this: cpc file_name
