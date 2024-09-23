"Method 1"
def isZeroSum(l):
    n=len(l)
    for i in range(n):
        for j in range(i+1,n+1):
            if sum(l[i:j])==0:
                return True
    return False
l=[1,4,13,-3,-10,5]
print(isZeroSum(l))

"Method 2"
def sumZero(l):
    pre_sum=0
    h=set()
    for i in range(len(l)):
        pre_sum=pre_sum+l[i]
        if pre_sum not in h and pre_sum!=0:
            h.add(pre_sum)
        else:
            return True
    return False
l=[1,4,13,-3,-10,5]
print(sumZero(l))