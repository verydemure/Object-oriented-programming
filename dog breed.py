class dog :
   species = "dog"

   def __init__(self,breed,anger,colour):
      self.breed = breed
      self.anger = anger
      self.colour = colour

rehan = dog("pitbull",50,"brown")
tahmid = dog("rottweiler",50,"black as hell")
ziba = dog("golden retriever",10,"brown")
zabihr = dog("german shepard",100,"black")

print()

print(f"rehans  is a {dog.species} ")
print(f"tahmids  is a {dog.species}")
print(f"zibas  is a {dog.species}")
print(f"zabhir is a {dog.species}")

print()

print(f"rehans breed is {rehan.breed}")
print(f"tahmids breed is {tahmid.breed}")
print(f"zibas breed is {ziba.breed}")
print(f"zabhir breed is {zabihr.breed}")

print()

print(f"rehans anger lever is {rehan.anger}")
print(f"tahmids anger level is {tahmid.anger}")
print(f"zibas angel level is {ziba.anger}")
print(f"zabhir anger level is {zabihr.anger}")

print()
print(f"rehans colour is {rehan.colour}")
print(f"tahmids colour is {tahmid.colour}")
print(f"zibas colour is {ziba.colour}")
print(f"zabhir colour is {zabihr.colour}")





