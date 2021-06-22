#Using the print keyword 
print("Hello World")
print()

#printing another string
#you can use print to print any string
print("My name is Athreya")
print()

#Using print for asking questions
print("What is your name?")
print()

#Using print to draw shapes
print("--------") #around 10
print("|      |")
print("|      |")
print("--------")
print()

print("|----/")
print("|   / ")
print("|  /  ")
print("| /   ")
print("|/    ")
print()

#Use print to print hangman
print("---------")
print("|       |")
print("|       o")
print("|      \|/")
print("|       |")
print("|      / \\")
print("|          ")  
print()

#Using print with single quotes
print('Printing with single quotes')

#Single quotes vs. Double quotes

print('That is very "funny"')
print("That is very 'funny'")


#----------------------Variables, dataTypes, Casting, fstrings-----------------------#
#Using Variables
name = "Bob"
print(name)

#Variables with multiple words
sister_name = "Kate"
#---------------------------Data Types-------------------------------------#

#integers
#5, 1, 2134, 423, 593

#lets start out with some basic integer operations

#Basic operations
int1 = 2
int2 = 5
int3 = 4
print(type(int1))

print(int1 * int2)
print(int1 + int2) 
print(int1 * (int2 + int3)) #PEMDAS
print(int2 % int1) #Mod

#Common methods
print(pow(3, 2))
print(max(5, 6))

#Strings
name = "Krish"
print(name)
print(type(name))

#Indexing and Slicing
print(name[0])  
print(name[4])
print(name[2:4]) #get characters from 2 to 4 (not included)
print(name[-1]) #gets last index
print(name[-2]) #gets second to last index
print(name[:]) #gets whole string

#Length
print(len(name))

#Common String methods
print(name.index("K"))
print(name.replace("Krish", "Bob")) #these give copies and does not modify name
print(name.lower()) 
print(name.upper())

#9.234, 5.5123, 6.43

#Basic operations
float1 = 3.14
float2 = 4.23
float3 = 9.82
print(type(float1))

print(float1 * float2)
print(float1 + float2) 
print(float1 * (float2 + float3)) #explain PEMDAS

#Common methods
print(pow(3, 2))
print(max(5, 6))
print(round(2.3))

#Boolean - True/False

is_raining = False
print(is_raining)
print(type(is_raining))

print(10 == 10)
print(10 > 9)
print(7 < 8)
print(8 <= 8)
print(10 >= 45)


#-------------------casting--------------------------------#


#Integers
a = int(1)   
b = int(2.8) 
c = int("3")

#Floats
d = float(1)     
e = float(2.8)   
f = float("3")   
g = float("4.2")

#Strings
h = str("s1") 
i = str(2)    
j = str(3.0)

#Practical application
age = 15
name = "Jack"
print("Hi, my name is " + name + ". I am " + str(age) + " years old.")

age1 = "18"
age2 = 14
age3 = 16
sum_of_ages = int(age1) + age2 + age3

print("The sum of ages of students in the class is " + str(sum_of_ages) + ".")

#------------------------------Fstring-----------------------------------


#F string
name = "Jeff"
print("My name is " + name)
print(f"My name is {name}")

#F string - casting benefit
age = 15
print("My age is " + str(15)) 
print(f"My age is {age}")



#---------------------------input------------------------------#

#Getting input from users
name = input("Enter in your name: ")
print(f"Hello {name}. Nice to meet you!")

#USER FORM PROJECT

name = input("What is your full name? ")
age = input("What is your age? ")
grade = input("What grade are you going to? ")
gender = input("What is your gender? ")

print(f"Hello {name}. You are {age} years old and you are a {gender}. You are going to go to grade {grade} next year. ")


#----------------------------------Conditionals------------------------#


#IF and IF-ELSE statments


#If statements
is_raining = True
if is_raining: # can be rewritten as just is_raining
    print("It is raining today.")

age_threshold = 20
age = 13
if age < age_threshold:
    print("You are a very young programmer!")

#And, or, not operations
is_tall = True
is_handsome = False

if is_tall and is_handsome:
    print("You are tall and handsome")
if is_tall or is_handsome:
    print("You are either tall or handsome")
if not is_tall:
    print("You are not tall")




#---IF else statements


#else statements
is_raining = True

if is_raining:
    print("It is raining")
else:
    print("It is not raining")

#elif statements

letter_a = 90
letter_b = 80
letter_c = 70
cur_grade = 87

if cur_grade > letter_a:
    print("You have an A in the class! Great job!")
elif cur_grade > letter_b: 
    print("You have a B in the class!")
elif cur_grade > letter_c: 
    print("You have a C in the class.")
else:
    print("You are not passing the class unfortunately... :(")



#------------------------------Lists------------------------------------#


#basic lists

#Initialize Lists
friends = ["Bob", "Jill", "Jack", "Jim"]

#Printing lists
print(friends)
num_friends = len(friends)
print(num_friends)

#Indexing into lists (similar to strings)
print(friends[0]) 
print(friends[-1])
print(friends[1:])
print(friends[1:3])

#Modify lists
friends[1] = "Krish"
print(friends)


#List operations

numbers = [1, 2, 3, 4, 5]
names = ["Bob", "Jill", "Jack", "Jim"]

#Append
names.append("Jack")
print(names)

#Insert
names.insert(2, "Jeff")
print(names)

#Remove
names.remove("Jeff")
print(names)

#Counting occurences
print(names.count("Jack"))

#Sort
numbers.sort()
names.sort()

print(numbers)
print(names)

#Reverse
numbers.reverse()
print(numbers)

#Clear
names.clear()
print(names)

#--------------------------------Dictionaries------------------------------#

#Dictionaries (like a list except the indices are what you choose)

age_translator = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

#Access items, keys, values
print(f"These are the items of the ageTranslator dictionary: {age_translator.items()}")
print(f"These are the keys of the ageTranslator dictionary: {age_translator.keys()}")
print(f"These are the values of the ageTranslator dictionary: {age_translator.values()}")

print()

#Only way to iterate over a dictionary
for key in age_translator:
    print(f"The value of {key} is {age_translator[key]}")
print(age_translator[:])
print()






#--------------------------Loops------------------------------------#

#Strings
message = "hello"
for letter in message: 
    print(letter)

#Numbers
for i in range(5):
    print(i)

for i in range(3, 10):
    print(i)

for i in range(0, 10, 2):
    print(i)

#While Loops

#Numbers
i = 1
while i <= 10:
    print(f"Value of i: {i}")
    i = i + 1

print()

#Break statement
j = 1
while True:
    print(f"Value of j: {j}")
    if j == 5:
        break #First show the loop as an infinite loop
    j = j + 1



#calculator project



should_continue = True

print("Hello! This is a calculator.")

while should_continue:
    print()
    operation = input('Would you like to add (type "a"), multiply (type "m"), or divide (type "d")?: ')
    if operation == "a":
        add1 = int(input("Enter in your first number you want to add: "))
        add2 = int(input("Enter in your second number you want to add: "))
        print(f"Here is the sum of the two numbers {add1 + add2}.")
    elif operation == "m":
        mult1 = float(input("Enter in your first number you want to multiply: "))
        mult2 = float(input("Enter in your second number you want to multiply: "))
        print(f"Here is the product of the two numbers {mult1 * mult2}.")
    elif operation == "d":
        div1 = float(input("Enter in your first number you want to divide: "))
        div2 = float(input("Enter in your second number you want to divide: "))
        print(f"Here is the quotient of the two numbers {div1 / div2}.")
    else:
        print('Please input an appropiate string! Either "a", "m", or "d"')

    stop = input('If you would like to exit and stop the program, type "stop", otherwise press enter: ')
    if(stop == "stop"):
        should_continue = False

print("Thank you for using our calculator game! Have a great day!")

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
