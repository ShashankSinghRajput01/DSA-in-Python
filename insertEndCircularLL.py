"Naive Sol Theta(n)"
class Node:
    def __init__(self,k):
        self.key=k 
        self.next=None
head = Node(10)
head.next= Node(20)
head.next.next= Node(30)
head.next.next.next= Node(40)
head.next.next.next.next= head
def printCircularList(head):
    if head == None:
        return
    print(head.key,end=" ")
    i=head.next
    while i != head:
        print(i.key,end=" ")
        i=i.next

def insertEndCircularLL(head,x):
    newNode=Node(x)
    if head==None:
        newNode.next=newNode
        return newNode
    curr=head
    while curr.next!=head:
        curr=curr.next
    newNode.next=head
    curr.next=newNode
    return head
    
print("Previous List:")
printCircularList(head)
head=insertEndCircularLL(head,5)
print("\nNew List:")
printCircularList(head)

"Efficient Sol Theata(1)"
class Node:
    def __init__(self,k):
        self.key=k 
        self.next=None
head = Node(10)
head.next= Node(20)
head.next.next= Node(30)
head.next.next.next= Node(40)
head.next.next.next.next= head
def printCircularList(head):
    if head == None:
        return
    print(head.key,end=" ")
    i=head.next
    while i != head:
        print(i.key,end=" ")
        i=i.next

def insertEndCircularLL(head,x):
    newNode=Node(x)
    if head==None:
        newNode.next=newNode
        return newNode
    else:
        newNode.next=head.next
        head.next=newNode
        head.key,newNode.key=newNode.key,head.key
        return newNode
    
print("\nPrevious List:")
printCircularList(head)
head=insertEndCircularLL(head,5)
print("\nNew List:")
printCircularList(head)