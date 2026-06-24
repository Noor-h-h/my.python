import string
alphabet=string.ascii_letters*2

massage=input("Enter a massage :")
shafit_number=int(input("Enter a shift number :"))

def info(massage,shafit_number): 
 encryption=""
 for letter in massage:
    if letter in alphabet:
        original_words=alphabet.index(letter)
        new_position=original_words+shafit_number
        encryption+=alphabet[new_position]
    
    else:
        encryption+=letter

 print(encryption)
info(massage,shafit_number)


