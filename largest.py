def largest(l):
    sum=len(l)
    for i in l:
        if i>sum:
            sum=i
    return sum
l=[10,20,30,40,43]
print(largest(l))
