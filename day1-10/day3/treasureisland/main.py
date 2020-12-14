print("*****Welcome to the Treasure island*****")
print("Your mission is to find the treasure.")
lr=input("You're at a cross road, Where do you want to go? Type 'left' or 'right '\n")
if(lr=='right'):
  print("Oops! yoe're fallen into a hole.... Game Over!")
if(lr=='left'):
  sw=input("You came to a lake,Do you want to 'swim' or 'wait'?\n")
  if(sw=='swim'):
    print("Attacked by a trout...Game Over!")
  if(sw=="wait"):
    rby=input("There are many doors of different colors choose any color you want to open? e.g red or blue or orange\n")
    if(rby=="red"):
      print("Oops! You're burned by fire,Game Over!")
    elif(rby=="blue"):
      print("You're eaten by beasts.Game Over!")
    elif(rby=="yellow"):
      print("Congratulations!!! You won the Game...Here your treasure is\n")
      print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')  
    else:
      print("Game Over!")



    
      


