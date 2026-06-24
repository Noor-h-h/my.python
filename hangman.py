import random
hangman_stage=['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


words=["good","bad","ugly"]
random_word=random.choice(words)
display=["_"]*len(random_word)
print(" ".join(display))
lives=6
gussed_letters=[]
print(hangman_stage[0])

while "_" in display and lives > 0 :
    gussed=input("Please guess a letter : ").lower()

    if gussed in gussed_letters:
       print("You alreadry guessed that. try again")
       print(f"You have {lives}more tries")

  
       continue

    gussed_letters.append(gussed)

    if gussed not in random_word:
        lives-=1
        print(hangman_stage[6-lives])
    else:
       for position in range(len(random_word)):
        if random_word[position]==gussed:
            display[position]=gussed


    print(''.join(display))
    print(f"You have {lives}more tries")

if lives==0:
   print("""
         You lose !
         """)
   print(hangman_stage[-1])
else:
   print("""
     *********
     You win
     *********
        """)
 

        