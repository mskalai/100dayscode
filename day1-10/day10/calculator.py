import art
from replit import clear
def operation(in1,in2,op):
  if op=="+":
    res=in1+in2
    return res
  if op=="-":
    res=in1-in2
    return res 
  if op=="*":
    res=in1*in2
    return res  
  if op=="/":
    res=in1/in2
    return res
nop=True
while(nop):
  print(art.logo)
  in1=float(input("What's the first number? "))
  opt=True      
  while(opt):
    print("\n+\n-\n*\n/")
    op=input("pick an opertaion ")
    in2=float(input("What's the next number? "))
    res=operation(in1,in2,op)
    print(f"{in1} {op} {in2} = {res}")
    con=input(f"Type 'y' to continue for calculating with {res}, or type 'n'  to start a new calculation: ")
    if con=='y':
      opt=True
      in1=res
    else:
      opt=False
      clear()
         