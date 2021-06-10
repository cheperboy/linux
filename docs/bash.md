# bash built-in

### Sed
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


### find

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

    [find with xarg and exec](https://www.grymoire.com/Unix/Find.html)

### grep

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

### xargs
Xargs executes its arguments as commands, and reads standard input to specify arguments to that command.  
Xargs knows the maximum number or arguments each command line can handle, and does not exceed that limit.
The following are equivalent

    find /tmp -print | xargs ls -ld
    ls -ld `find /tmp -print`


### mkdir

    mkdir -pv # create parent directory (verbose)

### rsync

    rsync -avzh  --progress                        #rsync-copy
    rsync -avzh  --progress --remove-source-files  #rsync-move
    rsync -avzhu --progress                        #rsync-update
    rsync -avzhu --progress --delete               #rsync-synchronize

    option utiles
    -------------
    -a : same as -rlptgoD
                 -r       : --recursive
                  -l      : keep sym link as they are 
                   -ptgoD : preserve owner group perms device time
    -s, --protect-args      : don't interpret wildcards in filename 
    -z, --compress
    -u, --update            : skip files that are newer on the receiver
    -n, --dry-run           : trial run with no changes made
    -i, --itemize-changes   : output a change-summary for all updates
    -H, --hard-links        : preserve hard links
    --remove-source-files   : sender removes synchronized files (non-dir)
    --delete                : delete extraneous files from dest dirs
    -v, --verbose
    -h, --human-readable
    --exclude=tmp/ 
    -backup --backup-dir=rsync_trash/ (use also --exclude=rsync_trash/ )
    --files-from=FILE : To specify the exact list of files to transfer 


    use rsync to make a diff (diff also permission, attributes, atime, ...)
    ------------------------
    rsync -aHAX -ni --delete
    

### web

    netstat -nat|grep -i ":80"|wc -l    # connections sur le port 80


## Administration

déplacer une partition https://www.linuxtricks.fr/wiki/ajouter-une-partition-home-ou-var-ou-autre-apres-installation  
chroot https://www.linuxtricks.fr/wiki/chrooter-un-systeme-linux  

### renommer plusieurs fichiers

    ls -c1 | xargs -I {} mv {} "prefixe{}suffixe"


### history sorted by occurence

    history | awk '{print $2;}' | sort | uniq -c | sort -rn | head -10

choisir **awk** ou **sed** pour avoir toute la ligne ou juste la commande

`awk '{print $2;}'`             récupère la commande qui est en deuxième colonne (exemple *ls*)  
`sed -e 's/ *[0-9][0-9]* *//'`  récupère toute la ligne de commande (exemple *ls -la*)  
`sort`      tri alphabetique  
`uniq -c`   supprime les doublons et ajoute une colonne avec le nombre d'occurence  
`sort -rn`  tri numérique (-n) inverse (-r)  
`head -10`  affiche uniquement les 10 premiers résultats


## bash Redirection

    > Overwrite  
    >> Append  
    command >file or command 1>file # Redirect stdout to file. stderr to console  
    command 2>file                  # Redirect stderr to file. stderr to console  
    command >file                   # Redirect stdout to file. stderr to console  
    command >file 2>&1              # Redirect stdout & stderr to file  
    command 2>&1 | tee -a file      # Redirect stdout & stderr console and append to file 
    command >/dev/null 2>&1         # Discard both stdout & stderr  

### Lister les répertoires vides

    find . -empty -type d

### Supprimer les répertoires vides

    find . -empty -type d -delete

### Supprimer les fichiers selon un motif

    find . -type f -name "motif" -print | xargs rm -f

### Chercher un motif dans des fichiers

    find . -type f -name '*.sql' | xargs grep 'foo.bar'

### Changer les droits des répertoires

    find /path/to/base/dir -type d -print0 | xargs -0 chmod 755
 ou
 
    find /path/to/base/dir -type d -exec chmod 755 {} +

### Changer les droits des fichiers

    find /path/to/base/dir -type f -print0 | xargs -0 chmod 644
 ou

    find /path/to/base/dir -type f -exec chmod 644 {} +
