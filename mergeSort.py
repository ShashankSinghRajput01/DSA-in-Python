def mergeSort(arr,l,r):
    if r>l:
        m=(l+r)//2
        mergeSort(arr,l,m)
        mergeSort(arr,m+1,r)
        mergeSubarrays(arr,l,m,r)
    return arr
    
def mergeSubarrays(a,low,mid,high):
    left=a[low:mid+1]
    right=a[mid+1:high+1]
    k=low
    i=0
    j=0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            a[k]=left[i]
            i=i+1
            k=k+1
            
        else:
            a[k]=right[j]
            j=j+1
            k=k+1
            
    while i<len(left):
        a[k]=left[i]
        i=i+1
        k=k+1
        
    while j<len(right):
        a[k]=right[j]
        j=j+1
        k=k+1
        
    
a=[10,12,23,30,11,23,43]
l=0
r=len(a)
print(mergeSort(a,l,r))
