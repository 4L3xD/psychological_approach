# Importante!
# Use as referências dos commits anteriores para construir a lógica, pois o código mais recente é menos intuitivo e mais abstrato ainda que seja mais eficiente!

import json
#from time import sleep
from random import randint
from approach import Approach

approach = Approach()

file = open("boas_vindas.txt", "r")
print(file.read())

with open("status.json") as jsonFile:
  json = json.load(jsonFile)

nome = input("Oi, qual é o seu nome? ")
print(f"{nome}, legal te conhecer!")

#sleep(1)

status = input("Eu sou Severina.\nComo você está? ")
for resp in json:
  if resp in status:
    #print(len(json[resp]))
    severina_resp = json[ resp ][ randint(0, len(json[resp]) - 1) ]
    print(severina_resp)
    if "?" in severina_resp:
      approach.Psychological_Approach(nome)

# Exemplos didáticos:
##  a = randint(0, 3)
##  print(json['bem'][a])

