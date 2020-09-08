import random
import string

working = True
while working == True:

    """
    This function is designated to help you create a randomized password with the length of your choosing.
    Args:
        length (int) = The lenth of the desired password
        wantNums (Requires a string value of 'y' or 'n') = This decides if you want to include any numbers in the password
        wantUppers (Requires a string value of 'y' or 'n') = This decides if you want it to have upper case letters
        wantSymbols (Requires a string value of 'y' or 'n') = This decides if you want any special characters 
    Returns:
        A password of your choosing depending on the options you have chosen
    """


    length = int(input("How long do you want the password to be? [in numbers]"))
    wantNums = input("Do you want numbers in the password? [y/n] ")
    wantUppers = input("Do you want uppercase letters? [y/n] ")
    wantSymbols = input("Do you want symbols? [y/n]")



    def passwordGen(length):

        if wantNums.lower() == "y" and wantUppers.lower() == "y" and wantSymbols.lower() == "n":
            password = ""
            chars = string.ascii_letters + "1234567890"
            symb = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~'"
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
            print(password)

        elif wantNums.lower() == "n" and wantUppers.lower() == "n" and wantSymbols.lower() == "y":
            password = ""
            chars = string.ascii_letters 
            symb = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~'"
            for i in range(length):
                password = password + random.choice(chars) + random.choice(symb)
            print(password)


        elif wantNums.lower() == "y" and wantUppers.lower() == "y" and wantSymbols.lower() == "y":
            password = ""
            chars = string.ascii_letters + "1234567890"
            symb = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~'"
            for i in range(length):
                password = password + random.choice(chars) + random.choice(symb)
            print(password)

        else:
            print("Invalid input, please enter [y/n]! ")


    passwordGen(length)

    restart = input("Do you want another password? [y/n] ")
    if restart.lower() == "y":
        working = True
    else:
        print("Goodbye!")
        working = False
