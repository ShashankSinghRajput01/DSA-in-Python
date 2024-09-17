import math
class Node:
    def __init__(self,key):
        self.data=key
        self.next=None

# head -> Front
# tail -> Rear

class MyQueue:
    def __init__(self):
        self.head=None
        self.tail=None
        self.sz=0
    
    def enque(self,x):
        temp=Node(x)
        if self.tail ==None:
            self.head=self.tail=temp
        else:
            self.tail.next=temp
            self.tail=temp
        self.sz=self.sz+1

    def size(self):
        return self.sz
    
    def deque(self):
        if self.head ==None:
            return math.inf
        res=self.head.data
        self.head=self.head.next
        if self.head==None:
            self.tail=None
        self.sz-=1
        return res
    
    def isEmpty(self):
        if self.sz>0:
            return False
        return True
    
    def getFront(self):
        if self.head==None:
            return math.inf
        else:
            return self.head.data
        
    def getRear(self):
        if self.head==None:
            return math.inf
        else:
            return self.tail.data
    
s=MyQueue()
s.enque(10)
s.enque(20)
s.enque(30)
print(s.deque())
print(s.size())
s.enque(40)
print(s.getFront())
print(s.getRear())
print(s.isEmpty())

