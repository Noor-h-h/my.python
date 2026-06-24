
class User:
        def __init__(self,first_name,last_name,email,password,status='inactive'):
            self.first_name=first_name
            self.last_name=last_name
            self.email=email
            self.password=password
            self.status = status



            

        def display_choice(self):
             
            print(f"Last Name: {self.last_name}")
            print(f"Email: {self.email}")
            print(f"Password: {self.password}")
            print(f"Status: {self.status}")
    

def create_user():
     

     print("Welcome to user management system ")
     first_name=input("Enter first name :")
     last_name=input("Enter last name :")
     email=input("Enter emial :")
     password=input("Enter password :")

     return User(first_name,last_name,email,password)
 
users=[]


choice=""
while choice !="3":
      print("Welcom to user managment")

      choice=input("""
1. Add new user 
2.Display all users
3.Exit 

             
 Enter your choice :""") 

      if choice=="1":

       user1 = create_user()
       users.append(user1)
       print("User added successfully.\n")
      elif choice=="2":
         if not users:
          print("\n No users founr \n")
         else:
          print("\n all users")
          for u in users:
               u. display_choice()

      elif choice=="3":
       print("Exit")

      else:
         print("Invilid")

     



      

    
