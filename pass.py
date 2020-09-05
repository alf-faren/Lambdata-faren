import random
import string

working = True
while working == True:


    length = int(input("How long do you want the password to be? [in numbers]"))
    wantNums = input("Do you want numbers in the password? [y/n] ")
    wantUppers = input("Do you want uppercase letters? [y/n] ")
    wantSymbols = input("Do you want symbols? [y/n]")



    def passwordGen(length):

        if wantNums.lower() == "y" and wantUppers.lower() == "y":
            password = ""
            chars = string.ascii_letters + "1234567890"
            for i in range(length):
                password = password + random.choice(chars)
            print(password)


        elif wantNums.lower() == "n" and wantUppers.lower() == "y" and wantSymbols.lower() == "y":
            password = ""
            chars = string.ascii_letters
            symb = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~'"
            for i in range(length):
                password = password + random.choice(chars) + random.choice(symb)
            print(password)

        elif wantNums.lower() == "y" and wantUppers.lower() == "n" and wantSymbols.lower() == "y":
            password = ""
            chars = string.ascii_letters + "1234567890"
            symb = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~'"
            for i in range(length):
                password = password + random.choice(chars) + random.choice(symb)
            print(password.lower())

        elif wantNums.lower() == "n" and wantUppers.lower() == "n" and wantSymbols.lower() == "y":
            password = ""
            chars = string.ascii_letters 
            symb = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~'"
            for i in range(length):
                password = password + random.choice(chars) + random.choice(symb)
            print(password.lower())

        elif wantNums.lower() == "y" and wantUppers.lower() == "y" and wantSymbols.lower() == "y":
            password = ""
            chars = string.ascii_letters + "1234567890"
            symb = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~'"
            for i in range(length):
                password = password + random.choice(chars) + random.choice(symb)
            print(password.lower())

        else:
            print("Invalid input, please enter [y/n]! ")


    passwordGen(length)

    restart = input("Do you want another password? [y/n] ")
    if restart.lower() == "y":
        working = True
    else:
        print("Goodbye!")
        working = False
