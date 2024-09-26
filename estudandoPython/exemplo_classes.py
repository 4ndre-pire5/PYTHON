# class Friend:
#     def __init__(self):
#         self.job = "None"
#         self.age = 0

#     def getJob(self):
#         return self.job

#     def setJob(self, job):
#         self.job = job

#     def getAge(self):
#         return self.age

#     def setAge(self, age):
#         self.age = age        


# Alice = Friend()
# Bob = Friend()

# Alice.setJob("Carpenter")
# Alice.setAge("25")
# Bob.setJob("Builder")
# Bob.setAge(33)

# print(Bob.job)
# print(Bob.age)
# print(Alice.job)
# print(Alice.age)

# class Music:
#     @staticmethod
#     def play():
#         print("*playing music*")

#     def stop(self):
#         print("stop playing")    

# Music.play() 
# # Music.stop()    # vai gerar um erro pois não existe um objeto criado

# obj = Music()
# obj.stop()    

# class Fruit:
#     name = 'Fruitas'

#     def printName(cls):
#         print("The name is: ", cls.name)

# Fruit.printAge = classmethod(Fruit.printName) 
# Fruit.printAge()

class Human:
    name = ""

class Coder:
    skills = 3

class Pythonista(Human, Coder):
    version = 3

obj = Pythonista()
obj.name = "Alice"

print(obj.name)
print(obj.version)
print(obj.skills)
