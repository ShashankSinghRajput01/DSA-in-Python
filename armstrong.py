def armStrong(n):
    p=str(n)
    q=len(p)
    sum=0
    for i in p:
        sum+=int(i)**q
    if n==sum:
        return True,sum
    else:
        return False,sum
    

n=int(input("write a no.: "))
print(armStrong(n))
