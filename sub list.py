def subList(l,x):
    sub=[]
    for i in l:
        if i<=x:
            sub.append(i)
    return sub
    
l=[10,12,13,14,15,28,68]
x=20
print(subList(l,x))