class MyQueue:
    def __init__(self,c):
        self.l=[None]*c
        self.cap=c
        self.sz=0
        self.front=0
        self.rear=0

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
        
    def isFull(self):
        return self.sz == self.cap
    
    def insertRear(self,x):
        if self.isFull():
            return
        else:
            rear=(self.front+self.sz-1)%self.cap
            rear=(rear+1)%self.cap
            self.l[rear]=x
            self.sz+=1

    def insertFront(self,x):
        if self.isFull():
            return
        else:
            self.front=(self.front-1)%self.cap
            self.l[self.front]=x
            self.sz+=1

        
    def deleteFront(self):
        if self.sz==0:
            return None
        else:
            res=self.l[self.front]
            self.sz-=1
            return res
        
    def deleteRear(self):
        if self.sz==0:
            return None
        else:
            rear=(self.front+self.sz-1)%self.cap
            res=self.l[rear]
            self.sz-=1
            return res
    
    def size(self):
        return self.sz
    
s=MyQueue(5)
s.insertFront(10)
s.insertRear(20)
s.insertFront(30)
print(s.deleteFront())
print(s.deleteRear())
print(s.size())
s.insertRear(40)
print(s.getFront())
print(s.getRear())
print(s.isEmpty())

