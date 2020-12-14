import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
l=int(input("How many letters would you like to insert in your password\n"))
s=int(input("How many symbols woukd you like to insert in your password\n"))
n=int(input("How many numbers woukd you like to insert in your password\n"))
lt=[]
for i in range(l):
  lt+=random.choice(letters)
for i in range(s):
  lt+=random.choice(symbols)  
for i in range(n):
  lt+=random.choice(numbers) 
random.shuffle(lt)
password=""
for i in lt:
  password+=i
print(f"Your password is {password}")


   


    
