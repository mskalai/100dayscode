import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
ch=[rock,paper,scissors]
ui=int(input("Enter you input for rock-0 for paper-1 for scissors-2\n"))
print(ch[ui])
ci=random.choice(ch)
print("computer chooses\n",ci)
if(ch[ui]==ci):
  print("Match draw")
if(ch[ui]==rock and ci==scissors):
  print("You win")
if(ch[ui]==scissors and ci==rock):
  print("Computer wins") 
if(ch[ui]==scissors and ci== paper):
  print("You win")
if(ch[ui]==paper and ci==scissors):
  print("Computer wins")
if(ch[ui]==paper and ci==rock):
  print("You win")
if(ch[ui]==rock and ci==paper):
  print("Computer wins")     
