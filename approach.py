class Approach():
    def __init__(self):
        pass
    def Psychological_Approach(self, name):
        user_resp = input()
        possible_resps = ["sim", "quero", "uhum", "me ajude", "não", "não quero"]
        if user_resp in possible_resps and "não" not in user_resp:
          print(f"Certo, {name}... vamos entender o que está acontecendo.")
        else:
          print(f"Tudo bem, {name}. A gente não precisa falar disso.")
        #return user_resp