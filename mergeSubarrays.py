def mergeSubarrays(a,low,mid,high):
    left=a[low:mid+1]
    right=a[mid+1:high+1]
    k=low
    i=0
    j=0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            a[k]=left[i]
            k=k+1
            i=i+1
        else:
            a[k]=right[j]
            k=k+1
            j=j+1
    while i<len(left):
        a[k]=left[i]
        k=k+1
        i=i+1
    while j<len(right):
        a[k]=right[j]
        k=k+1
        j=j+1
    return a
a=[1,2,3,44,12,23,34,56]
low=0
high=9    
mid=3
print(mergeSubarrays(a,low,mid,high))