# create a class called person with name,age,gender as
# the attribe a construtor, a method and an object
from oop import myobj


class Person:
    #constractor method
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

#method
    def display(self):
        print( f"Our youngest staff {self.name}, is {self.age} years and identifies as {self.gender}")
#structure
myobj=Person("Elvis",20,"female")
myobj.display()