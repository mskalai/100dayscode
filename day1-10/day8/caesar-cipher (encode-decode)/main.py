import art 
from alphabets import alphabet
def caesar(text,shift,direction):
  msg=str()
  out=[]
  for ab in text:
    for tx in ab:
      for i in tx:
        if i in alphabet:
          pos=alphabet.index(i)
          if direction=="encode":
            if(pos+shift<25):
              msg+=alphabet[pos+shift]
            else:
              msg+=alphabet[(pos+shift)%25]
          else: 
            if(pos-shift<0):
              msg+=alphabet[25-abs(pos-shift)]
            else:
              msg+=alphabet[(abs(pos-shift))%25]
        else:
          msg+=i         
      out.append(msg)
      msg=" "    
  print(f"The {direction}d message is",*out) 
def function():
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  text = [input("Type your message:\n").lower().split(' ')]
  shift = int(input("Type the shift number:\n"))
  caesar(text,shift,direction)
  lp=input("enter 'yes' to if you want to continue or press 'no'\n").lower()
  if(lp=="yes"):
   function()
  else:
    print("GoodBye") 
print(art.logo)
function()

    

