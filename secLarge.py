def secLarge(l):
    if len(l)<=1:
        return None
    larg=max(l)
    slar=None
    for i in l:
        if i!=larg:
            if slar==None:
                slar=i
            else:
                slar=max(slar,i)
    return slar
l=[1,2,3,4,5]
print(secLarge(l))
        
    