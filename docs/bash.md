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

## Sed example
Substitute (find and replace) "foo" with "bar" on each line

    sed 's/foo/bar/'             # replaces only 1st instance in a line
    sed 's/foo/bar/4'            # replaces only 4th instance in a line
    sed 's/foo/bar/g'            # replaces ALL instances in a line
    sed 's/\(.*\)foo\(.*foo\)/\1bar\2/' # replace the next-to-last case
    sed 's/\(.*\)foo/\1bar/'            # replace only the last case

Substitute "foo" with "bar" ONLY for lines which contain "baz"

    sed '/baz/s/foo/bar/g'

Substitute "foo" with "bar" EXCEPT for lines which contain "baz"

    sed '/baz/!s/foo/bar/g'

Change "scarlet" or "ruby" or "puce" to "red"

    sed 's/scarlet/red/g;s/ruby/red/g;s/puce/red/g'   # most seds
    gsed 's/scarlet\|ruby\|puce/red/g'                # GNU sed only



## bash Redirection

`>` Overwrite  
`>>` Append  

`command >file` or `command 1>file` Redirect stdout to file. stderr to console  
`command 2>file` Redirect stderr to file. stderr to console  
`command >file` Redirect stdout to file. stderr to console  

`command >file 2>&1` Redirect stdout & stderr to file  
`command 2>&1 | tee -a file` Redirect stdout & stderr console and append to file 

`command >/dev/null 2>&1` Discard both stdout & stderr  


## bash onliner

### history sorted by occurence

    history | awk '{print $2;}' | sort | uniq -c | sort -rn | head -10

choisir **awk** ou **sed** pour avoir toute la ligne ou juste la commande

`awk '{print $2;}'` récupère la commande qui est en deuxième colonne (exemple *ls*)  
`sed -e 's/ *[0-9][0-9]* *//'` récupère toute la ligne de commande (exemple *ls -la*)  
`sort` tri alphabetique  
`uniq -c` supprime les doublons et ajoute une colonne avec le nombre d'occurence  
`sort -rn` tri numérique (-n) inverse (-r)  
`head -10` affiche uniquement les 10 premiers résultats

