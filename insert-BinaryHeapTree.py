class MyMinHeap:
    def __init__(self):
        self.arr=[]
    def parent(self,i):
        return(i-1)//2
    def lChild(self,i):
        return (i*2+1)
    def rChild(self,i):
        return (i*2+2)
    def insert(self,x):
        arr=self.arr
        arr.append(x)
        i=len(arr)-1
        while i>0 and arr[self.parent(i)]>arr[i]:
            p=self.parent(i)
            arr[i],arr[p]=arr[p],arr[i]
            i=p
s=MyMinHeap()
s.arr=[10,80,15,100,85,18]
s.insert(12)
print(s.arr)