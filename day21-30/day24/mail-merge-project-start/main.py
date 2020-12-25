with open(r"C:\Users\MS Kalai\Downloads\mail-merge-project-start\Input\Names\invited_names.txt") as names:
    names=names.readlines()
with open(r"C:\Users\MS Kalai\Downloads\mail-merge-project-start\Input\Letters\starting_letter.txt") as startlet:
    letter=startlet.read()

for name in names:
    name_strip=name.strip()
    with open(rf"C:\Users\MS Kalai\Downloads\mail-merge-project-start\Output\ReadyToSend\{name_strip}","w+") as invite:
        invite.write(letter.replace("[name]",name_strip))






