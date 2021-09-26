import json
import sys
import os
import subprocess as sp
from random import randint

class Severina():
    def __init__(self, name):
        try:
            memory = open(name+'.json', 'r')
        except FileNotFoundError:
            memory = open(name+'.json', 'w')
            memory.write('[["Severina"], {"oi": "Oie! 😋", "tchau": "Tchau! Tchau! 😘"}]')
            memory.close()
            memory = open(name+'.json', 'r')
        self.name = name
        self.known, self.phrases = json.load(memory)
        memory.close()
        self.historic = [None]


    def listen(self, phrase=None):
        if phrase == None:
            phrase = input('>: ')
        phrase = str(phrase).lower()
#        phrase = phrase.lower()
        return phrase


    def think(self, phrase):
        if phrase in self.phrases:
            return self.phrases[phrase]
        if phrase.lower() == 'aprende':
            return """🤓 O que você quer que eu aprenda?\n\nDefina em uma palavra!"""
        if phrase == 'jogar':
            games = ["https://brunolemos.github.io/trust/", "https://ncase.itch.io/wbwwb"]
            theGame = games[ randint( 0, len(games) -1 ) ]
            return f"Divirta-se!\n{theGame}"
        if phrase == 'aprender':
            tools = ["https://brilliant.org/", "https://www.kaggle.com/", "https://www.khanacademy.org/", "https://exercism.org/", "https://www.hackerrank.com/"]
            theTool = tools[ randint( 0, len(tools) -1 ) ]
            return f"Bons estudos!\n{theTool}"

        # historic
        lastPhrase = self.historic[-1]
        
        if 'Oie! ' in lastPhrase:
            return 'Qual é o seu nome?'

        if lastPhrase == 'Qual é o seu nome?':
            name = self.getName(phrase)
            response = self.answerName(name)
            return response

        if 'O que você quer que eu aprenda?' in lastPhrase:
            self.key = phrase
            #implementar chamada pelo nome
            return f'O que é {phrase}?'

        if 'O que é ' in lastPhrase:
            response = phrase
            self.phrases[self.key] = response
            self.saveMemory()
            return 'Aprendido!'
        try:
            response = str(eval(phrase))
            return response
        except:
            pass
        return 'Não entendi...'


    def getName(self, name):
        if 'Meu nome é ' in name:
            name = name[12:]
        name = name.title()
        return name


    def answerName(self, name):
        if name in self.known:
            if name != 'Severina':
                phrase = 'Eaew, '
            else:
                phrase = 'E se somos Severinas iguais em tudo na vida, morreremos de morte igual, mesma morte severina.'
        else:
            phrase = 'Muito prazer, '
            self.known.append(name)
            self.saveMemory()
        return phrase + name + '!'
    

    def saveMemory(self):
        memory = open(self.name+'.json', 'w')
        json.dump([self.known, self.phrases], memory)
        memory.close()
    

    def speak(self, phrase):
        if 'Executa ' in phrase:
            platform = sys.platform
            command = phrase.replace('Executa ', '')
            if 'win' in platform:
                os.startfile(command)
            if 'linux' in platform:
                try:
                    sp.Popen(command)
                except FileNotFoundError:
                    sp.Popen(['xdg-open', command])
        else:
            print(phrase)
        self.historic.append(phrase)