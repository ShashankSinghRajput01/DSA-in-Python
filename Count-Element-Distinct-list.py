"Method 1"
def cDinstinct(l):
    res=1
    for i in range(1,len(l)):
        if l[i] not in l[:i]:
            res+=1
        else:
            return res
l=[1,2,3,4,5,5]
print(cDinstinct(l))        


"Method 2"
l=[1,2,3,4]
print(len(set(l)))
