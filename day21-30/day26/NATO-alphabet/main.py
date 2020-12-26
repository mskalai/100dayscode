import pandas
nato=pandas.read_csv("nato_phonetic_alphabet.csv")
data=pandas.DataFrame(nato)
dict={val.letter:val.code for (key,val) in data.iterrows()}
name=input("Enter a word ").upper()
res=[dict[let] for let in name]
print(res)
