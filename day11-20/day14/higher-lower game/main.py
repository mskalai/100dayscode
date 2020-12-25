from art import logo,vs
import random
from gamedata import data
from replit import clear
game=True
while(game):
  con=True
  cs=0
  clear()
  print(logo)
  while(con):
    data1=random.choice(data)
    data2=random.choice(data)
    print(f"Compare A :{data1['name']} ,{data1['description']} ,{data1['country']}")
    print(vs)
    print(f"Against B :{data2['name']} ,{data2['description']} ,{data2['country']}")
    max=''
    if data1['follower_count'] > data2['follower_count'] :
      max='a'
    else:
      max='b'   
    guess=input("Who has more followers? type 'A' or 'B' :").lower()
    if guess==max:
      cs+=1
      clear()
      print(logo)
      print(f"You are right, Current score : {cs}")
      con=True
    else:
      clear()
      print(logo)
      print(f"Sorry,You are wrong, Final score : {cs}")
      con=False
      game=input("Do you want to play again? Tap 'y' or 'n' :").lower()
      if game=='y':
        game=True
      else:
        game=False    
    






