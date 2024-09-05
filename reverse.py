def reverse(l):
    s=0
    e=len(l)-1
    while s < e :
        l[s],l[e]=l[e],l[s]
        s=s+1
        e=e-1
    return l
l=[1,2,3,4]
print(reverse(l))    
