"Method 1"
def leftShiftOne(l):
    for i in range (1,len(l)):
        l[i],l[i-1]=l[i-1],l[i]
    return l
l=[1,2,3,4,5]
print(leftShiftOne(l))

"Method 2"
l=[1,2,3,4,5]
l=l[1:]+l[0:1]
print(l)

"Method 3"
l=[1,2,3,4,5]
l.append(l.pop(0))
print(l)

"Method 4"
def rotateByOne(l):
    n=len(l)
    x=l[0]
    for i in range(1,n):
        l[i-1]=l[i]
    l[n-1]=x
    return l
l=[1,2,3,4,5]
print(rotateByOne(l))