print("******Welcome to the Love Calculator!******")
n1=input("What is your name?\n")
n2=input("What is your partner name?\n")
l1=0
l2=0
l1=n1.lower().count('t')+n1.lower().count('r')+n1.lower().count('u')+n1.lower().count('e')
l2=n2.lower().count('t')+n2.lower().count('r')+n2.lower().count('e')+n2.lower().count('u')
l=l1+l2
l3=n1.lower().count('l')+n1.lower().count('o')+n1.lower().count('v')+n1.lower().count('e')
l4=n2.lower().count('l')+n2.lower().count('o')+n2.lower().count('v')+n2.lower().count('e')
o=l3+l4
re=int(str(l)+str(o))
if(re<10 or re>90):
  print(f"Your score is {re}%, you go together like coke and mentos")
elif(re>40 and re<50):
  print(f"Your score is {re}%, you are alight together.")
else:
  print(f"Your score is {re}%")