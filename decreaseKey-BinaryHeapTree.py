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
        
s=MyMinHeap()
s.arr=[10,20,40,80,100,70]
s.decreaseKey(3,5)
print(s.arr)