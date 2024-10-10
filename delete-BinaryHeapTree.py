import math
class MyMinHeap:
    def __init__(self):
        self.arr=[]
    def parent(self,i):
        return(i-1)//2
    def lChild(self,i):
        return (i*2+1)
    def rChild(self,i):
        return (i*2+2)
    
    def decreaseKey(self,i,x):
        arr=self.arr
        arr[i]=x
        while i!=0 and arr[self.parent(i)]>arr[i]:
            p=self.parent(i)
            arr[i],arr[p]=arr[p],arr[i]
            i=p

    def minHeapify(self,i):
        arr=self.arr
        lt=self.lChild(i)
        rt=self.rChild(i)
        smallest=i
        n=len(arr)
        if lt<n and arr[lt]<arr[smallest]:
            smallest=lt
        if rt<n and arr[rt]<arr[smallest]:
            smallest=rt
        if smallest!=i:
            arr[smallest],arr[i]=arr[i],arr[smallest]
            self.minHeapify(smallest)

    def extractMin(self):
        arr = self.arr
        arr[0],arr[-1]=arr[-1],arr[0]   
        # We can also assign instead of Swapping
        res = arr[-1]
        arr.pop()
        self.minHeapify(0)
        return res
    
    def delete(self,i):
        n=len(self.arr)
        if i>n:
            return None
        else:
            self.decreaseKey(i,-math.inf)
            self.extractMin()

s=MyMinHeap()
s.arr=[5,9,8,12,14,20,40]
s.delete(1)
print(s.arr)