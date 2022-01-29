## Shell config

install zsh and ohmyzsh  
call personal profile from `~/.zshrc` (see `.cheperboy_profile.sh`)  
update `/etc/zsh/zshenv` (see exemple given) to set the PATH   

**memo about bash vs zsh dotfiles loading**  
bash loads `/etc/profile` `~/.profile` `~/.bashrc`  
zsh loads `/etc/zsh/zshenv` `~/.zprofile` `~/.zshrc`  

## Prompt

type in console to see and add in perso profile to make permanent 

### basic Prompt

	SIMPLE_PROMPT="%~ %# "
	PROMPT="%F{green}$USER%f@%F{blue}%m %f%~ %# "

| arg | desc | 
| --- | ---- | 
| %F{green} | set color |
| $USER | print user name |
| %f | reset color |
| @ | print @ |
| %F{blue} | set color | 
| %m | print hostname  |
| %f | reset color |
| %~ | print current working dir |
| %# | print a prompt () |


### git support
 
	PROMPT='%(!.%{%F{yellow}%}.)$USER @ %{$fg[white]%}%M %{$fg_bold[red]%}➜ %{$fg_bold[green]%}%p %{$fg[cyan]%}%c %{$fg_bold[blue]%}$(git_prompt_info)%{$fg_bold[blue]%} % %{$reset_color%}'


	%~	current working dir, shortening home to ~
	%1~	current working dir, shortening home to ~, show only last 1 element
	%#	# with root privileges, % otherwise
	%(?.√.?%?)	if return code ? is 0, show √, else show ?%?
	%?	exit code of previous command
	%B %b	start/stop bold
	%F{green}	color foreground
	$fg[green]%} color foreground (alternative)
	%f	reset to default textcolor


## highlight (colorized cat)

Install

	sudo apt-get install highlight

Usage

	highlight -O ansi script.py

If extenstion is unknown, use `--force` to print anyway
To specify syntax, use `--syntax=bash`

Shell config

	alias cat="highlight -O ansi --force"
	alias bcat="highlight -O ansi --syntax=bash"


## Logiciels de base
`sound-juicer` mp3 ripper  
`handbrake` dvd ripper  
`mkusb` usb bootable persistent https://doc.ubuntu-fr.org/mkusb  
`BackInTime` Sauvegarde de donénes    
`timeshift` Sauvegarde du système et fichiersde conf système
`conky`  


