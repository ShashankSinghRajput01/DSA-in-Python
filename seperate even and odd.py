def evenOdd(a):
    even=[]
    odd=[]
    for x in a:
        if x%2==0:
            even.append(x)
        else:
            odd.append(x)
    return even,odd
a,b=evenOdd([10,12,13,25,34,36,29])
print("even",a)
print("odd",b)
