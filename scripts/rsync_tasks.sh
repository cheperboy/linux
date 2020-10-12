#!/bin/bash

# Sauvegarde de dossiers avec rsync
# Appel du script
# ./rsync_tasks.sh 2>&1 | tee -a rsync_tasks.log

###################################
# Rappel de quelques option rsync #
###################################
# --size-only       
#   saute les fichiers qui sont similaires par la date
#   Normalement rsync ignore tous les fichiers qui ont la même taille et une horodate identique. Avec l'option --size-only, les fichiers seront ignorés s'ils ont la même taille, indépendamment de l'horodate. Ceci est utile lorsque l'on commence à se servir de rsync après avoir utilisé un autre outil de miroitage qui peut ne pas préserver les horodates exactement. 

#--backup-dir=REP   
#   utilisé avec l'option --backup, ceci dit à rsync de garder garder les fichiers supprimés dans le répertoire spécifié

############################
# Fonctionnement du script #
############################
# Utilisation de l'option --backup et --backup-dir :
# Les fichiers supprimés de SOURCE ne sont pas supprimé sur DEST mais
# sont déplacés vers DEST/TRASH_DIR
# $TRASH_DIR est donc exclut des dossiers traités par rsync afin de ne pas le supprimer de DEST
#
# Chaque tache possède son fichier log dans le répertoire du script
#
# Ajouter la ligne suivante pour faire un test:
#--dry-run \
#

TRASH_DIR=".rsync_trash/"

#Redirect stdout and stderr to console and also append to log file 
function ECHO ()
{
echo $1 2>&1 | tee -a rsync_tasks.log
}

function Unset ()
{
unset TASK
unset SOURCE
unset DEST
unset LOGFILE
}

function Rsync ()
{
declare task=$1
declare source=$2
declare logfile=$3
declare dest=$4
declare trash=$5

ECHO "-----------------"
ECHO "${task}"

rsync \
--recursive \
-x --verbose \
--progress \
--delete \
--size-only \
--exclude=@eaDir/ \
--filter "- lost+found/" --filter "- .cache/" \
--backup --backup-dir=$trash \
--exclude=$TRASH_DIR \
--log-file=$logfile \
$source \
$dest

ECHO "Done ${task}"
ECHO ""
}

ECHO "-------------------------------"
ECHO "Starting rsync tasks `date +%F`"
ECHO ""

: '
TASK="test"
SOURCE="/home/cheperboy/Documents/backtest/"
LOGFILE="/home/cheperboy/rsync_backup/task_${TASK}.log"
DEST="/home/cheperboy/Documents/backtest_dest"
TRASH="/home/cheperboy/Documents/backtest_dest/${TRASH_DIR}"
Rsync $TASK $SOURCE $LOGFILE $DEST $TRASH
Unset;
'

TASK="archives"
SOURCE="/media/cheperboy/data_ssd/Archives/"
LOGFILE="/home/cheperboy/rsync_backup/task_${TASK}.log"
DEST="/media/NAS_ORS/backup/Archives"
TRASH="${DEST}/${TRASH_DIR}"
Rsync $TASK $SOURCE $LOGFILE $DEST $TRASH
Unset;

TASK="documents"
SOURCE="/media/cheperboy/data_ssd/documents/"
LOGFILE="/home/cheperboy/rsync_backup/task_${TASK}.log"
DEST="/media/NAS_ORS/backup/documents"
TRASH="${DEST}/${TRASH_DIR}"
Rsync $TASK $SOURCE $LOGFILE $DEST $TRASH
Unset;

TASK="images_divers"
SOURCE="/media/cheperboy/data_ssd/Images/Divers/"
LOGFILE="/home/cheperboy/rsync_backup/task_${TASK}.log"
DEST="/media/NAS_ORS/photo/Divers"
TRASH="${DEST}/${TRASH_DIR}"
Rsync $TASK $SOURCE $LOGFILE $DEST $TRASH
Unset;

TASK="images_matcha"
SOURCE="/media/cheperboy/data_ssd/Images/mat&cha/"
LOGFILE="/home/cheperboy/rsync_backup/task_${TASK}.log"
DEST="/media/NAS_ORS/photo/mat&cha"
TRASH="${DEST}/${TRASH_DIR}"
Rsync $TASK $SOURCE $LOGFILE $DEST $TRASH
Unset;

