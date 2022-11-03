#!/bin/sh

#####################################################################
#
# script name: start.sh
# created in: 21/19/22
# modified in: 09:14:41
#
# summary: inicia o projeto de ia do machado de assis
#                                               developed by: bates
#####################################################################

#variables
DATE=$(date)

if [ $?  -eq 0 ]
then
    clear
    echo "Checking dependencies"
    sleep 1
    if source assistent_virtual/env/env.sh
    then
        sleep 1
        echo "Running the scripts"
        sleep 1
        python3 assistent_virtual/scripts/python/assistent.py 2> /dev/null
    else
        echo "Something went wrong"
        fi
else
    echo "You ran the program wrong!"
fi



