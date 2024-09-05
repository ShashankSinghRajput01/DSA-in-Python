def average(l):
    n=len(l)
    sum=0
    for i in l:
        sum+=i
    return sum/n
l=[2,3,4,5]
print(average(l))