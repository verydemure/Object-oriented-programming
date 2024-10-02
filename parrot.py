class Parrot:

    #class Variable
    species = "bird"

    # Constructor Method 
    def __init__(self,name,age):
        self.name = name
        self.age = age


blu = Parrot("blu" , 10)
woo = Parrot("woo" , 16)


print(f"Blu is a {blu.species}")
print(f"woo is also a {blu.species}")

print(f"{blu.name} is {blu.age} years old")

print(f"{woo.name} is {woo.age} years old")

