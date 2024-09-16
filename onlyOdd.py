def onlyOdd(l):
    for x in l:
        y=l.count(x)
        if y%2 !=0:
            return x
    else:
        return None
l=[10,10,20,30,30,20,40]
print(onlyOdd(l))
        

"OR,OR,OR,OR"

def findOdd(l):
    res=0
    for x in l:
        res=res ^ x
    return res
l=[10,20,20,30,10]
print(findOdd(l))