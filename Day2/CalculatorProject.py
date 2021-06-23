
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
