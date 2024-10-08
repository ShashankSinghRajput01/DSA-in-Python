class MyMinHeap:
    def __init__(self):
        self.arr=[]
    def parent(self,i):
        return(i-1)//2
    def lChild(self,i):
        return (i*2+1)
    def rChild(self,i):
        return (i*2+2)
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

s=MyMinHeap()
s.arr=[20,25,30,35,40,80,32,100,70,60]
print(s.extractMin())
print(s.arr)