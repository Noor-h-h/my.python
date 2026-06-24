import random

rock_ascii=("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")


paper_ascii=("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")


Scissors_ascii=("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")


print("Welcom to the Rock,Paper , Sissors game")
confirme=input("Press Enter to continue or type (Help) for the rules ")

# اذا كان المتغير كونفيرم جاوبت بهيلب يطبعلي الشروط وبعدها ينطيني المتغير يوز جويز حتى اختار
#واذا المتعير مو نفس اللي اريده يطبعلي انفايلد
if confirme == "help" :
    print("""                 *********RULES*********
          1) You choose and the computer chooses
          2) Rock smashes Scissors -> Rock wins 
          3) Scissors cut Paper -> scissors win
          4) Paper covers Rock -> paper wins""")
user_choce=input("Enter your choice (Rock , Paper , Sissors): ").capitalize()

#اذا المتغير مو نفس الكلمات اللي اريدها يطبعلي انفايدلد
if user_choce not in ["Rock" , "Paper" , "sissors" ]:
    print ("Invalid choice . Please run the program again choose rock , paper , or scissors . ")

#والا اذا نفس الكلمه اللي اريدها يطبع خيارات انه اليوز جويس شنو ممكن يساوي 
else : 
    if user_choce =="Rock":
        print(f" \n you choce :\n{rock_ascii}")
    elif user_choce == "Paper":
        print(f" \n you choce :\n{paper_ascii}")
    else:
        print(f" \n you choce :\n{Scissors_ascii}")

#بعدها اسوي نفس الشي اطبع اذا الكومبيوتر جويس شنو ممكن يساوي 
computer_choice = random.choice(["rock","paper","scissors"])
if computer_choice =="Rock":
        print(f" \n you choce :\n{rock_ascii}")
elif computer_choice == "Paper":
        print(f" \n you choce :\n{paper_ascii}")
else:
        print(f" \n you choce :\n{Scissors_ascii}")

#بعدها اطبع الحالات اللي ممكن الشخص يفوز بيها او لا
#اذا كان اختيار الكمبتوتر نفس اختيار الشخص نكول تعادل 
if user_choce==computer_choice: 
     print("It is a tie!")

#واما اذا كانت الاختيارات مختلفه لازم نطبع احتماله الفوز 
elif(
     (user_choce =="rock" and computer_choice =="scissors")
     or 
     (user_choce == "paper" and computer_choice =="rock")
     or 
     (user_choce == "scissors" and computer_choice=="paper")
): 
     print(f"you win! {user_choce} beats {computer_choice}")

#اذا احتماليه الفوز مصارت نطبع خسارى 
else:
     print(f"you lost! {computer_choice} beats {user_choce}")