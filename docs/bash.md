
## Command line tools

[awesome-shell](https://github.com/alebcay/awesome-shell)  
[awk](https://en.wikibooks.org/wiki/AWK)  
[grep](https://alvinalexander.com/unix/edu/examples/grep.shtml)  

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

    sed 's/foo/bar/'                    # replaces only 1st instance in a line
    sed 's/foo/bar/4'                   # replaces only 4th instance in a line
    sed 's/foo/bar/g'                   # replaces ALL instances in a line
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

    > Overwrite  
    >> Append  
    command >file or command 1>file # Redirect stdout to file. stderr to console  
    command 2>file                  # Redirect stderr to file. stderr to console  
    command >file                   # Redirect stdout to file. stderr to console  
    command >file 2>&1              # Redirect stdout & stderr to file  
    command 2>&1 | tee -a file      # Redirect stdout & stderr console and append to file 
    command >/dev/null 2>&1         # Discard both stdout & stderr  


## bash onliner

### history sorted by occurence

    history | awk '{print $2;}' | sort | uniq -c | sort -rn | head -10

choisir **awk** ou **sed** pour avoir toute la ligne ou juste la commande

`awk '{print $2;}'`             récupère la commande qui est en deuxième colonne (exemple *ls*)  
`sed -e 's/ *[0-9][0-9]* *//'`  récupère toute la ligne de commande (exemple *ls -la*)  
`sort`      tri alphabetique  
`uniq -c`   supprime les doublons et ajoute une colonne avec le nombre d'occurence  
`sort -rn`  tri numérique (-n) inverse (-r)  
`head -10`  affiche uniquement les 10 premiers résultats

## find

    ls -ld $(find .)    # ls recursif

    find /var -iname "*.log"                        # Lister les fichiers nommés *.log dans /var (-iname: ignore case)
    find /var -iname "*.log" 2> /dev/null           # Ignorer les erreurs "permission non accordée"
    find ~/Téléchargements -size +20M -size -40M    # Taille entre 10 et 20 Mo

    find /var/log/ -atime -1      # fichiers modfiés il y a moins de 1 jour (aujourd'hui)
    find /var/log/ -atime +90     # fichiers modfiés il y a plus de 90 jours

    find /tmp -type f -name "*.log" -exec chown adrien {} \;    # Executer une commande: {} est remplacé par le nom de fichier. 
    find /tmp -type f -name "*.log" -exec rm -i {} \;

    -atime : date d'accès  
    -ctime : date de création  
    -mtime : date de modification  
    -type d : directory  
    -type f : file  
    -empty : fichier/dossier vide

## grep

    options
    -------
    -i case insensitive
    -H show filename
    -n show line numbers
    -v reverse regex pattern (find lines not containing)

    search string in files
    ----------------------
    grep 'hello.*world' *.log       # list all lines containing "Hello, world" (-i ignore case)
    grep -r 'foo' /home/mydir       # search recursively in mydir/
    grep -C 2 'foo' test*.log       # print context around the match

    regular expressions
    -------------------
    grep '^fred' /etc/passwd             # find 'fred', but only at the start of a line
    grep '[FG]oo' *                      # find Foo or Goo in all files in the current dir
    grep '[0-9][0-9][0-9]' *             # find all lines in all files in the current dir with three numbers in a row


mkdir -pv # create parent directory (verbose)

## rsync

    rsync -avz --progress -h                        #rsync-copy
    rsync -avz --progress -h --remove-source-files  #rsync-move
    rsync -avzu --progress -h                       #rsync-update
    rsync -avzu --delete --progress -h              #rsync-synchronize


## web

    netstat -nat|grep -i ":80"|wc -l    # connections sur le port 80

