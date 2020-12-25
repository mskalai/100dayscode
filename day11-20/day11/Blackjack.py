import random
from art import logo
from replit import clear
def calc(cards):
  if sum(cards)==21 and len(cards)==2:
    return 0
  if sum(cards)>21 and 11 in cards:
    cards.remove(11)
    cards.append(1)
    return(sum(cards))  
  else:   
    return sum(cards)
def result(ucs,ccs):
   if(ucs==0):
     print("Blackjack! You win.")
   elif(ccs==0):
     print("Computer has blackjack! You lose")
   elif(ucs==ccs):
     print("Match Draw")
   elif(ucs>21):
     print("You went over You lose!")
   elif(ccs>21):
      print("Computer went over! You win!!!")
   elif(ccs>21) and (ucs>21):
     print("You lose")   
   elif(ucs>ccs):
      print("You win")
   else:
     print("You lose") 
def display(uc,ucs,ccs): 
  print(f"Your cards: {uc}, current_score : {ucs}" )
  print(f"computer's first card : {cc[0]}" ) 
con=True
while(con):   
  gi=input("Do you want to plack Blackjack game? Tap 'y' or 'n' ")
  if(gi=='y'):
    clear()
    print(logo)  
    print("    Welcome to blackjack game!!     ")
    cc=[]
    uc=[]
    utc=True
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    for i in range(0,2):
      cc.append(random.choice(cards))
      uc.append(random.choice(cards))
    ucs=calc(uc)
    ccs=calc(cc) 
    display(uc,ucs,ccs)
    while(utc):
      if(ucs<=21) and ucs!=0 and ccs!=0: 
        ic=input("Type 'y' to get another card, type 'n' to pass ")
      else:
        result(ucs,ccs)
        utc=False 
        break
#condition when n given        
      if(ic=='n'):
        print(f"Your final hand: {uc}, final score, {ucs}")
        if(ccs<17) and ccs!=0:
          cc.append(random.choice(cards))
          ccs=calc(cc)
          print(f"computer's final hand: {cc}, final score, {ccs}")
          result(ucs,ccs)
          utc=False
        else:
          print(f"computer's final hand: {cc}, final score, {ccs}")
          result(ucs,ccs) 
          utc=False
#condition when y given          
      if(ic=='y'):
        uc.append(random.choice(cards))
        ucs=calc(uc)
        print(f"Your cards {uc}, current score: {ucs}")
        print(f"computer's first card : {cc[0]}" )
        if(ucs>21):
          print(f"Your final hand: {uc}, final score, {ucs}")
          print(f"computer's final hand: {cc}, final score, {ccs}") 
          result(ucs,ccs)
          utc=False
        elif(ccs<17) and ccs!=0:
            cc.append(random.choice(cards))
            ccs=calc(cc)
        else:
          print(f"computer's final hand: {cc}, final score, {ccs}")    
          utc=False  
          result(ucs,ccs)
    
            
  else:
    con=False        

        





