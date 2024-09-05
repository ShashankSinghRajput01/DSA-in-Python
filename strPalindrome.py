s=input("Enter a String: ")
p=0
e=len(s)-1
while p<e:
    if s[p]!=s[e]:
        print("Not a Palindrome")
        break
    p=p+1
    e=e-1
else:
    print("Its Palindrome")

