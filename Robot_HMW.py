class robot:

    def __init__ (self, name):
       self.name = name


tom = robot("Tom")
print("Hi, I am a robot.")
print ("My name is", tom.name)

jerry = robot("Jerry")
print("\nHi, I am also a robot.")
print ("My name is ", jerry.name)