## Command line tools

[awesome-shell](https://github.com/alebcay/awesome-shell)  
[awk](https://en.wikibooks.org/wiki/AWK)  
[grep](https://en.wikibooks.org/wiki/Grep)  

### sed
[wikibooks](https://en.wikibooks.org/wiki/Sed)  
[sed1line.txt](http://www.pement.org/sed/sed1line.txt)  
Sed One-Liners Explained article: 
[Part One](https://catonmat.net/sed-one-liners-explained-part-one), 
[Part Two](https://catonmat.net/sed-one-liners-explained-part-two), 
[Part Three](https://catonmat.net/sed-one-liners-explained-part-three).  
[Tutorial](https://www.grymoire.com/Unix/Sed.html)  


### bash
bash One-Liners Explained article: 
[Part One](https://catonmat.net/bash-one-liners-explained-part-one), 
[Two](https://catonmat.net/bash-one-liners-explained-part-two), 
[Three](https://catonmat.net/bash-one-liners-explained-part-three), 
[Four](https://catonmat.net/bash-one-liners-explained-part-four), 
[Five](https://catonmat.net/bash-one-liners-explained-part-five), 
[Six](https://catonmat.net/bash-one-liners-explained-part-six).  
[bash redirections cheatsheet](https://catonmat.net/ftp/bash-redirections-cheat-sheet.pdf)

### grep


## bash Redirection

`>` Overwrite  
`>>` Append  

`command >file` or `command 1>file` Redirect stdout to file. stderr to console  
`command 2>file` Redirect stderr to file. stderr to console  
`command >file` Redirect stdout to file. stderr to console  

`command >file 2>&1` Redirect stdout & stderr to file  
`command 2>&1 | tee -a file` Redirect stdout & stderr console and append to file 

`command >/dev/null 2>&1` Discard both stdout & stderr  
