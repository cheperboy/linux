## Command line tools

* [awesome-shell](https://github.com/alebcay/awesome-shell)
* [sed](https://en.wikibooks.org/wiki/Sed)
* [awk](https://en.wikibooks.org/wiki/AWK)
* [grep](https://en.wikibooks.org/wiki/Grep)


## Redirection

[bash-one-liners-explained](https://catonmat.net/bash-one-liners-explained-part-three)

`>` Overwrite  
`>>` Append  

`command >file` or `command 1>file` Redirect stdout to file. stderr to console  
`command 2>file` Redirect stderr to file. stderr to console  
`command >file` Redirect stdout to file. stderr to console  

`command >file 2>&1` Redirect stdout & stderr to file  

`command >/dev/null 2>&1` Discard both stdout & stderr  
	