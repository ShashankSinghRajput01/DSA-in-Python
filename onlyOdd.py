def onlyOdd(l):
    for x in l:
        y=l.count(x)
        if y%2 !=0:
            return x
    else:
        return None
l=[1,2,3,4,5,5,6]
print(onlyOdd(l))
        