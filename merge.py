arr1=[1,3,2,4,4]
arr2=[5,6,7,8]
w=arr1+arr2
w.sort()
print(w)

"OR,OR OR OR"


def mergelists(a,b):
    res=[]
    m=len(a)
    n=len(b)
    i=0
    j=0
    while i<m and j<n:
        if a[i] <b[j]:
            res.append(a[i])
            i=i+1
        else:
            res.append(b[j])
            j=j+1
    while i<m:
        res.append(a[i])
        i=i+1
    while j<n:
        res.append(b[j])
        j=j+1
    return res
a=[1,2,3,4,5]
b=[5,6,7,8,8]
print(mergelists(a,b))



