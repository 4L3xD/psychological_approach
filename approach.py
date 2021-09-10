import json
#from time import sleep
from random import randint
 
file = open("boas_vindas.txt", "r")
print(file.read())

with open("status.json") as jsonFile:
  json = json.load(jsonFile)

def Psichological_Approach():
  user_resp = input()
  possible_resps = ["sim", "quero", "uhum", "me ajude", "não", "não quero"]
  if user_resp in possible_resps and "não" not in user_resp:
    print("Certo... vamos entender o que está acontecendo.")
  else:
    print("Tudo bem. A gente não precisa falar disso.")
  #return user_resp

nome = input("Oi, qual é o seu nome? ")
print(f"{nome}, legal te conhecer!")

#sleep(1)

status = input("Eu sou Severina.\nComo você está? ")
for resp in json:
  if status == resp:
    #print(len(json[resp]))
    severina_resp = json[resp][randint(0, len(json[resp]) - 1)]
    print(severina_resp)
    if "?" in severina_resp:
      Psichological_Approach()
       
     
#a = randint(0, 3)
#print(json['bem'][a])

