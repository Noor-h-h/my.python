import time 
def validate_email(email):
    if "@" in email and "." in email:
        return True 
    else:
        return False


def add_user(name,email):
    if validate_email(email):
        print(f"User with{name} and email{email}  is succsfully")

    else:
        print(f"Invalid email format for user{name} Registration failed")

user_name=input("Enter a user name :")
user_email=input("Enter your email :")

print("chacking user name...")
time.sleep(3)
print("Validating email adress...")
time.sleep(3)


#ياخذ قيم اليوز نيم واليوزر ايميل يخليهم بالفاكشن بمتغيرات اسمها نيم وايميل 
add_user(user_name,user_email)