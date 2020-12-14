print("Welcome to the tip calculator.")
amt=int(input("What was the total bill? Rs."))
tp=int(input("What percentage tip would you like to give? 10, 12, or 15?"))
rtp=amt*tp/100
ppl=int(input("How many people to split the bill?"))
res=rtp/ppl
print(f"Each person should pay:Rs.{res}")
