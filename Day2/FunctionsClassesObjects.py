#-------------------------------Functions, Classes and Objects


#Functions
def test():
    print("Hello World")

test()

#Parameters
def introduction(name, age):
    print(f"This is {name} who is {age} years old")

introduction("Jeff", 15)

#Return 
def exponent(base, exp):
    finalAnswer = 1
    for i in range(exp):
        finalAnswer *= base
    return finalAnswer

exp = exponent(4, 2)
print(exp)


#Classes

#Computers.py
class Computer:
    def __init__(self, os, year_bought, is_powerful):
        self.os = os
        self.year_bought = year_bought
        self.is_powerful = is_powerful
#Student.py
class Student:
    def __init__(self, name, grade, gpa, is_funny):
        self.name = name
        self.grade = grade
        self.gpa = gpa
        self.is_funny = is_funny

#Main.py
from Students import Student
from Computers import Computer

student1 = Student("Jeff", 10, 3.8, False)
student2 = Student("Jill", 12, 3.4, True)
print(student1.name)
print(student1.isFunny)
print(student2.grade)
print(student2.gpa)

computer1 = Computer("Mac", 2016, True)
computer2 = Computer("Windows", 2013, False)
print(computer1.os)
print(computer2.isPowerful)




#Object Functions

#Main.py
from Radio import Radio

radio = Radio("The Box", 98.3)
print(radio.channel)

print(radio.is_good_song(radio.cur_song))

#Radio.py
class Radio:
    def __init__(self, cur_song, channel):
        self.cur_song = cur_song
        self.channel = channel
    
    def is_good_song(self, song):
        if song.lower() == "animals" or song.lower() == "the box":
            return True
        else:
            return False
