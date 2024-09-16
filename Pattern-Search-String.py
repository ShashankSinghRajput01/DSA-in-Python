txt=input("Enter text: ")
pat=input("Enter Pattern: ")
pos=txt.find (pat)
while pos>=0:
    print(pos)
    pos=txt.find(pat,pos+1)