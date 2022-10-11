import random

input("roll the dice? y/n ")

#setting the intitial response to y
response = "y"


while response == "y":
    #creating a random dice number
    number = random.randint(1,6)
    
    if (number == 1):
        print("|  *  |")
    elif (number==2):
        print("| *   |\n")
        print("|   * |")
    elif(number==3):
        print("| *   |\n")
        print("|  *  |\n")
        print("|   * |\n")
    elif(number==4):
        print("| * * |\n")
        print("| * * |")
    elif(number==5):
        print("| * * |\n")
        print("|  *  |\n")
        print("| * * |")
    elif(number==6):
        print("| * * |\n")
        print("| * * |\n")
        print("| * * |")

    response = input("press y to continue or n to exit ")
if response == "n":
    print("thanks for playing")