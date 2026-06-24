import os 
import random


def great():
    if os.name=="nt":
        os.system("cls")
    else:
        os.system("clear")

number_ran=random.randint(1,10)
Guess=int(input("Guess the number between 1 and 10 :"))

while Guess != number_ran:
     print("Wrong ")
     input("Press any key to continue....")
     great()
     Guess=int(input("Guess the number between 1 and 10 :"))

     if Guess == number_ran:
      print("you win")