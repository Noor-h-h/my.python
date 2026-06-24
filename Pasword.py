import random
import string
number=[0,1,2,3,4,5,6,7,8,9]
pasword="" 


print("Welcome to the password generator !")
total_number=int(input("Enter of characters in the password :"))
letters=int(input("Enter the number of letters in the password :"))
numbers=int(input("Enter the number of numbers in the password :"))
symbols=int(input("Enter the number of the symbols in the password :"))


if letters+numbers+symbols==total_number:
   random_letters=random.choices(string.ascii_letters,k=letters)
   random_numbers=random.choices(number,k=numbers)
   random_symbols=random.choices(string.punctuation,k=symbols)
   random_total=random_letters+random_numbers+random_symbols
   random_random=random.shuffle(random_total)
   
   
   for x in random_total:
    pasword+=str(x)
   print(pasword)


else:17
print("Invalid input. the sum of letters, numbers, and symbols soesnt match the password length.")