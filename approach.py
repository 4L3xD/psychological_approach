import sys, os
import subprocess as sp
from time import sleep
class Approach():
    def __init__(self):
      pass

    def Possible_Answer(self, user_answer):
      possible_answer = ["sim", "quero", "uhum", "me ajud", "não", "não quero"]
      for answer in possible_answer:
        if answer in user_answer:
          return answer

    def Game(self, name):
        print(f"Tudo bem, {name}. A gente não precisa falar disso.")
        showThing = input("Ei, posso te mostrar uma coisa? ")
        
        platform = sys.platform
        # Abre uma janela no navegador com um jogo
        if "não" not in self.Possible_Answer(showThing):
          print("É um dos meus jogos favoritos! Vamos lá!")
          sleep(2)
          if "win" in platform:
            os.startfile("https://brunolemos.github.io/trust/")
          elif 'linux' in platform:
            try:
              sp.Popen("https://brunolemos.github.io/trust/")
            except FileNotFoundError:
              sp.Popen(['xdg-open', "https://brunolemos.github.io/trust/"])

    def Psychological_Approach(self, name):
      user_answer = input()
      
      if "não" not in self.Possible_Answer(user_answer):
        print(f"Certo, {name}... vamos entender o que está acontecendo.")
        what_is_happening = input("O que você está sentindo? ")

      else:
        self.Game(name)
