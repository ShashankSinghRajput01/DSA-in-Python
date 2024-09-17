class MyQueue:
    def __init__(self,c):
        self.l=[None]*c
        self.cap=c
        self.sz=0
        self.front=0

    def getFront(self):
        if self.sz==0:
            return None
        else:
            return self.l[self.front]
    
    def getRear(self):
        if self.sz==0:
            return None
        else:
            rear=(self.front+self.sz-1)%self.cap
            return self.l[rear]
        
    def isEmpty(self):
        if self.sz>0:
            return False
        else:
            return True
    
    def enque(self,x):
        if self.sz==self.cap:
            return
        else:
            rear=(self.front+self.sz-1)%self.cap
            rear=(rear+1)%self.cap
            self.l[rear]=x
            self.sz+=1
        
    def deque(self):
        if self.sz==0:
            return None
        else:
            res=self.l[self.front]
            self.front=(self.front+1)%self.cap
            self.sz-=1
            return res
    
    def size(self):
        return self.sz
    
s=MyQueue(5)
s.enque(10)
s.enque(20)
s.enque(30)
print(s.deque())
print(s.size())
s.enque(40)
print(s.getFront())
print(s.getRear())
print(s.isEmpty())

