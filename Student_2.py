class student:
    grade = 9
    name = "Saahir"

    def introduction(self):
        print("Hi, I am a student.")

    def intro(self):
        print("My name is", self.name)
        print("I am in grade", self.grade)
    
obj = student()
obj.introduction()
obj.intro()