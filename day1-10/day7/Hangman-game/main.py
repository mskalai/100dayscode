import random
import hangman_words as hw
import hangman_art as ha
from replit import clear
wo=hw.words
logo=ha.logo
stages=ha.stages
w=random.choice(wo)
print(logo)
#print(f"The chosen word is {w}")
cw=[]
for i in range(len(w)):
   cw.append('_')
st=6   
cn=True  
while "_" in cw: 
 if(cn):
  k=input("Guess the letter ").lower() 
  clear()
  pos=-1
  for j in w:
    pos+=1
    if k==j:
      cw[pos]=k
  if k in w:
    print(*cw)    
  else:
    st-=1
    print(stages[st])
  if(st>=1):
    cn=True
  else:
    cn=False 
    print("You lose") 
    break
    
if "_" not in cw:
 print("you win")   
     
      
   
     
    
