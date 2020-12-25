import random
from replit import clear
from art import logo
def level(num,lvl):
  if lvl=="easy":
    attempts=5
  else:
    attempts=10  
  guess=int(input("Make a guess "))
  while guess!=num:
    if(guess>num):
      print("Too high")
    else:
      print("Too low")
    print(f"you have {attempts} attempts left")
    guess=int(input("Guess again "))  
    attempts-=1
    if attempts==0:
      print(f"You lost! The answer is {num}")
      break
  if guess==num:
    print(f"You got it! The answer is {num}")
entry=True
while(entry):
  print(logo)     
  print("Welcome to the Number Guessimng game")
  print("I am thinking a number between 1 and 100")
  num=random.randrange(1,100)
  lvl=input("Choose the difficulty level 'easy' or 'hard' ").lower()
  level(num,lvl)
  con=input("Do you want to play again? tap 'yes' or 'no' ").lower()
  if con=="yes":
    entry=True
    clear()
  else:
    entry=False 


