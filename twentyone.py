import random
def deal_card():

    cards=[11,2,3,4,5,6,7,8,9,10,10,10]
    card=random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)




def compare(user_score,computer_score):
    results={
        "draw":"Draw \n\n",
        "user_over":"You went over 21 , sorry \n\n",
        "computer_over":"Computer went over 21 , you win \n\n",
        "user_21":"You won with a blackjack \n\n",
        "computer_21":"Sorry,computer had blackjack \n\n",
        "user_win":"You win \n\n",
        "user_lose":"You lose\n\n"
    }

    if user_score == computer_score:
        return results["draw"]
    
    elif user_score>21:
        return results["user_over"]
    elif computer_score >21:
        return results["computer_over"]
    elif user_score==0:
        return results["user_21"]
    elif computer_score==0:
        return results["computer-21"]
    elif user_score>computer_score:
        return results["user_win"]
    else:
        return results["user_lose"]
    

def game():
  user_card=[deal_card() for _ in range (2)]
  computer_cards=[deal_card() for _ in range (2)]
  game_continue=True
  while game_continue:
      user_score=calculate_score(user_card)
      computer_score=calculate_score(computer_cards)
      print(f"\n\n\nYour cards are{user_card},current score is {sum(user_card)}")
      print(f"computer first card is {computer_cards[0]}")
      if user_score == 0 or computer_score ==0 or user_score>21 or computer_score>21:
       
        game_continue=False

      else:
          user_need_another_card=input("Get another card y/n?").lower()
          if user_need_another_card == 'y':
              user_card.append(deal_card())
          else:
              game_continue=False
  while computer_score != 0 and computer_score<17:
      computer_cards.append(deal_card())
      computer_score=calculate_score(computer_cards)

  print(f"your final hand : {user_card} with score{user_score} ")
  print(f"computer final hand : {computer_cards} with score {computer_score}")
  print(compare(user_score,computer_score))
while input("Choose agame to start ....\n\n1-Froggy \n2-Twenty one \n3-Snake").lower() == "twenty one":
    game()





