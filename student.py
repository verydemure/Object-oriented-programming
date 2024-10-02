class Student:

    #class Variable
    grade = 8
    print("Hello i am a student of grade " ,grade)

    #constructor Method(Funtion)
    def __init__(self, name, age):
        self.name = name
        self.age = age


#creating object
zabir = Student("ZHR",25)
radoya =Student("coqutte gal",144)
tabid =Student("tabid",15)

print(zabir.name,zabir.age)
print(radoya.name,radoya.age)
print(tabid.name,tabid.age)