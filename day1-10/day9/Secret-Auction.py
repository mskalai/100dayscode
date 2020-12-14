from replit import clear
import art
print(art.logo)
print("Welcome to the secret auction program.")
auction=[]
opt=True
while(opt):
  name=input("What is your name? ")
  bid=int(input("What's your bid? "))
  nominees={name:bid}
  auction.append(nominees)
  cont=input("Are there any bidders? Type 'yes' or  'no' ").lower()
  if cont=="yes":
    opt=True
    clear()
  else:
    clear()
    opt=False
ma=0
for dic in auction: 
  for i in dic:
    if ma<dic[i]:
      ma=dic[i]
      key=i
for dic in auction: 
  if key in dic:
    print(f"The winner is {key} whose amount is {dic[key]}")     
      
    

   
          
    
