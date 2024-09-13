class Node:
    def __init__(self,key):
        self.key=key
        self.prev=None
        self.next=None
head=Node(10)
temp1=Node(20)
temp2=Node(30)
head.next=temp1
temp1.prev=head
temp1.next=temp2
temp2.prev=temp1

def printList(head):
    i=head
    while i != None:
        print(i.key,end=" ")
        i=i.next

def insertBegDLL(head,x):
    newNode=Node(x)
    if head==None:
        return newNode
    
    else:
        curr=head
        newNode.next=head
        head.prev=newNode
        return newNode
    
"OR OR OR OR"
def insertBegDLL(head,x):
    temp=Node(x)
    if head!=None:
        head.prev=temp
    temp.next=head
    return temp
    
print("\nPrevious List:")  
printList(head)
head=insertBegDLL(head,5)
print("\nNew List:")
printList(head)


