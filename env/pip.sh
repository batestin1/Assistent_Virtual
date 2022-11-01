#!/bin/sh

#####################################################################
#
# script name: pip.sh
# created in: 21/19/22
# modified in: 09:14:41
#
# summary: checa se existe os pips necessarios para instalação do software
#                                               developed by: bates
#####################################################################

#variables

SR=$(pip show SpeechRecognition)

if $SR == $(sed -n '1p')
then
    echo "speech_recognition is installed"
else 
then
    pip install SpeechRecognition
fi

PR=$(pip show playsound)

if $SR == $(sed -n '1p')
then
    echo "playsound is installed"
else 
then
    pip install playsound=1.2.2
fi

gt=$(pip show gtts)

if $SR == $(sed -n '1p')
then
    echo "gtts is installed"
else 
then
    pip install gtts
fi

py=$(pip show pyttsx3)

if $SR == $(sed -n '1p')
then
    echo "pyttsx3 is installed"
else 
then
    pip install pyttsx3
fi


joblib=$(pip show joblib)

if $SR == $(sed -n '1p')
then
    echo "joblib is installed"
else 
then
    pip install joblib
fi

pillow=$(pip show pillow)

if $SR == $(sed -n '1p')
then
    echo "pillow is installed"
else 
then
    pip install pillow
fi

pip-chill=$(pip show pip-chill)

if $SR == $(sed -n '1p')
then
    echo "pip-chill is installed"
else 
then
    pip install pip-chill
fi

pyaudio=$(pip show pyaudio)

if $SR == $(sed -n '1p')
then
    echo "pyaudio is installed"
else 
then
    brew install pyaudio
    pip install pyaudio
fi

regex=$(pip show regex)

if $SR == $(sed -n '1p')
then
    echo "regex is installed"
else 
then
    pip install regex
fi

speech-recognition-fork=$(pip show speech-recognition-fork)

if $SR == $(sed -n '1p')
then
    echo "regex is speech-recognition-fork"
else 
then
    pip install speech-recognition-fork
fi

tqdm=$(pip show tqdm)

if $SR == $(sed -n '1p')
then
    echo "regex is tqdm"
else 
then
    pip install tqdm
fi