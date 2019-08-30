#!/usr/bin/env python

# Python 3 script template

import sys
import os
import click
import logging
from time import sleep
from tqdm import tqdm   # So simple console progress bar
import pathlib          # Simple path utility
import shutil           # shell utility eg : shutil.copytree(src, dest)

# Script Constants
MY_CONSTANT = 10

###############################################################################
# Configure logger
###############################################################################
logger = logging.getLogger(__name__)            # Gets or creates a logger (can replace __name__ by __file__)
logger.setLevel(logging.INFO)                   # set log level

# create console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)          # set level to debug
console_formatter = logging.Formatter('%(levelname)s : %(message)s') # create formatter
console_handler.setFormatter(console_formatter) # add console_formatter to console handler
logger.addHandler(console_handler)              # add console to logger

# create file handler and set formatter
file_handler = logging.FileHandler('logfile.log')
formatter    = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# Logs messages example
# logger.debug('A debug message')
# logger.info('An info message')
# logger.warning('Something is not right.')
# logger.error('A Major error has happened.')
# logger.critical('Fatal error. Cannot continue')
###############################################################################

#########################################
def calculate_with_exception_handling(my_int):
#########################################
    """ Docstring Short description
    Long Description
    """
    if my_int is not None:
        try:
            resultat = MY_CONSTANT / my_int
            logger.info(f'No error raised !')
        except ZeroDivisionError as e:
            logger.error(f'Exception ZeroDivisionError with my_int')
        except Exception as e:
            logger.error(f'Exception {e}', exc_info=True)
            raise # print traceback / raise to higher level
        else:
            print(f'{MY_CONSTANT}/{my_int} = {resultat}')
    else:
        raise IOError # Raise an exception to be catch at higher level !


@click.command()
@click.option('-f', '--input_file',     type=click.File('r'),   required=False)
@click.option('-d', '--destination',    type=click.STRING,      help='dest path')
@click.option('-i', '--value',          type=click.INT,         help='integer')
@click.option('-b', '--my_bool',        type=click.BOOL,        help='print progress bar')
#########################################
def my_function(input_file, destination, value, my_bool):
#########################################
    """ Docstring Short description
    Long Description
    """
    calculate_with_exception_handling(value)
    
    if input_file:
        click.echo(f'input_file : {input_file.name}')
    
    # Print a progress bar
    if my_bool:
        for key in tqdm(range(1)):
            sleep(0.01)
    
    # use pathlib
    if input_file:
        dest = pathlib.Path(destination).expanduser().resolve()
        dest = dest / 'usr/dir'
        if not dest.is_dir():
            exit(f"Dest directory {dest} does not exist.")
        click.echo(f'STDOUT message {destination}')

if __name__ == '__main__':
    my_function()
