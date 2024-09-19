import math
class Node:
    def __init__(self,key):
        self.data=key
        self.next=None
        self.prev=None

class MyDeque:
    def __init__(self):
        self.front=None
        self.rear=None
        self.sz=0
    
    def insertFront(self,x):
        temp=Node(x)
        if self.front==None:
            self.front=self.rear=temp
        else:
            temp.next=self.front
            self.front.prev=temp
            self.front=temp
        self.sz+=1

    def insertRear(self,x):
        temp=Node(x)
        if self.front==None:
            self.front=self.rear=temp
        else:
            temp.prev=self.rear
            self.rear.next=temp
            self.rear=temp
        self.sz+=1

    def getFront(self):
        if self.front==None:
            return math.inf
        return self.front.data

    def getRear(self):
        if self.front==None:
            return math.inf
        return self.rear.data
    
    def deleteFront(self):
        if self.front==None:
            return math.inf
        else:
            val=self.front.data
            self.front=self.front.next
            if self.front==None:
                self.rear=None
            self.sz-=1
            return val

    def deleteRear(self):
        if self.rear==None:
            return math.inf
        else:
            val=self.rear.data
            self.rear=self.rear.prev
            if self.rear==None:
                self.front=None
            self.sz-=1
            return val
    
    def size(self):
        return self.sz
    
    def isEmpty(self):
        if self.sz>0:
            return False
        return True
        
    
d=MyDeque()
d.insertFront(5)
d.insertFront(20)
print(d.getFront())
d.insertRear(10)
print(d.getRear())
print(d.deleteFront())
print(d.getFront())
d.deleteFront()
print(d.getFront())
d.insertFront(12)
d.deleteRear()
print(d.getRear())
print(d.getFront())
print(d.isEmpty())
print(d.size())
