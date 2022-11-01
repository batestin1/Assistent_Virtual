#!/usr/local/bin/python3
                        
                        #********************************************************************************#
                        #                                                                                #
                        #                                  нεℓℓσ,вαтεs!                                  #
                        #                                                                                #
                        #   filename: assistent.py                                                       #
                        #   created: 2022-03-10                                                          #
                        #   system: Darwin                                                               #
                        #   version: 64bit                                                               #
                        #                                       by: Bates <https://github.com/batestin1> #
                        #********************************************************************************#
                        #                           import your librarys below                           #
                        #********************************************************************************#


import speech_recognition as sr
import playsound
from gtts import gTTS
import random
import webbrowser
import pyttsx3
import os
from datetime import datetime
import locale

#definition of region
locale.setlocale(locale.LC_ALL, 'pt_BR')


class Assistent():
    def __init__(self,name_assistent, person) -> None:
        self.person = person
        self.name_assistent = name_assistent

        self.engine = pyttsx3.init()
        self.r = sr.Recognizer()
        self.voice_data = ''

    def engine_speach(self, text):
        #"voice of assistent_virtual"

        text = str(text)
        self.engine.say(text)
        self.engine.runAndWait()
    
    def record_audio(self,ask=""):
        with sr.Microphone() as source:
            if ask:
                print(ask)
                self.engine_speak(ask)

            audio = self.r.listen(source,5,5)
           

            try:
                self.voice_data = self.r.recognize_google(audio,language='pt-BR')
            except sr.UnknownValueError:
                text_sorry = ["Desculpa, não entendi", "Poderia falar novamente ?", "Desculpa, não consegui entender o que você quis dizer"]
                self.engine_speach(f"{self.person}, {random.choice(text_sorry)}")
            except sr.RequestError:
                self.engine_speach(f"Desculpa, meu servidor caiu!")
            print(">>", self.voice_data.lower())
            self.voice_Data = self.voice_data.lower()

            return self.voice_data.lower()

    def engine_speak(self, audio_string):
        audio_string = str(audio_string)
        tts = gTTS(text=audio_string, lang='pt')
        num = random.randint(1,20000)
        audio_file = f"audio_{str(num)}.mp3"
        tts.save(audio_file)
        playsound.playsound(audio_file)
        print(f"{self.name_assistent}: {audio_string}")
        os.remove(audio_file)

    def there_exist(self, terms):
        #"function to check if terms exist or not"
    
        for term in terms:
            if term in self.voice_data:
                return True
    
    def respond(self, voice_data):
        if self.there_exist(["oi", "olá", "oi tudo bem", "olá tudo bem", "tudo bem como vai", "tudo bem", "como vai", "fala", "tá aí", "e aí", "saudações", "namastê", "beleza", "diga"]):
            greetings = [f'Olá {self.person}, eu sou a {self.name_assistent} como vai você hoje?',
            f'E ai {self.person}, como posso te ajudar? ',
            f'Saudações {self.person}, como vamos hoje?',
            f'Namastê para você, {self.person}, no que posso ser útil?',
            f'Olá, meu nome é {self.name_assistent} como posso te ajudar?']
            greet = greetings[random.randint(0,len(greetings)-1)]
            self.engine_speach(greet)

        if self.there_exist(['procure por']) and 'youtube' not in voice_data:
            search_term = voice_data.split('por')[-1]
            url = f'http://google.com/search?q={search_term}'.lower()
            webbrowser.get().open(url) #open pages on google
            self.engine_speach(f"Aqui está o resultado que eu encontrei para {search_term} com google")

        if self.there_exist(['procure no youtube']):
            search_term = voice_data.split('youtube')[-1]
            url = f'http://youtube.com/results?search_query={search_term}'.lower()
            webbrowser.get().open(url) #open pages on google
            self.engine_speach(f"Aqui está o resultado que eu encontrei para {search_term} no youtube")
        
        if self.there_exist(['Que horas são']):
            search_term = voice_data[0]
            hour = datetime.now().strftime('%H')
            mn = datetime.now().strftime('%M')
            sec = datetime.now().strftime('%S')
            day = datetime.now().strftime('%d')
            month = datetime.now().strftime('%B')
            year = datetime.now().strftime('%Y')

            if hour in ['06', '07', '08', '10', '11']:
                self.engine_speach(f"Agora, ainda é dia. E são precisamente {hour} horas, {mn} min e {sec} segundos, do dia {day} de {month.capitalize()} do ano {year} do calendário cristão")
            elif hour in ['12', '13', '14', '15', '16', '17']:
                self.engine_speach(f"Agora é o periodo da Tarde, e são precisamente: {hour} horas, {mn} min e {sec} segundos, do dia {day} de {month.capitalize()} do ano {year} do calendário cristão")
            else:
                self.engine_speach(f"Agora já é Noite, e é precisamente: {hour} horas, {mn} min e {sec} segundos, do dia {day} de {month.capitalize()} do ano {year} do calendário cristão")


        
name_her = input("Enter with the name of your assistent: ").capitalize()
your_name = input("Enter with your name: ").capitalize()
assistent = Assistent(name_her,your_name)

while True:
    sp = ['pode falar agora', 'recomeçando', 'diga algo', 'fale']
    voice_data = assistent.record_audio(random.choice(sp))
    assistent.respond(voice_data)

    if assistent.there_exist(["fechar", "cancelar", "adeus", "até mais", "desligar programa", "desligar", "fica quieta", "cala-se", "silêncio"]):
        assistent.engine_speach("Entendi o recado, desligando...")
        break






'''
for i in mic:
    if sr.Microphone(i) == '[Errno -9998]':
        print('erro')
    else:
        with sr.Microphone(i) as source:
            voice = audio.listen(source)
            command = audio.recognize_google(voice, language='pt-BR')
            command = command.lower()
            machine.say(command)
            print(command)
            machine.runAndWait()



with sr.Microphone() as source:
    voice = audio.listen(source)
    command = audio.recognize_google(voice, language='pt-BR')
    command = command.lower()
    machine.say(command)
    print(command)
    machine.runAndWait()
    
        



try:
    with sr.Microphone() as source:
        print("Listening...")
        voice = audio.listen(source)
        command = audio.recognize_google(voice, language='pt-BR')
        command = command.lower()   
        if 'lily' in command:
            com
         

except:
    print("Trouble on your mic")
    
'''