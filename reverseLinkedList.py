class Node:
    def __init__(self,k):
        self.key=k 
        self.next=None
head = Node(10)
head.next= Node(20)
head.next.next= Node(30)
head.next.next.next= Node(40)

def printList(head):
    i=head
    while i != None:
        print(i.key,end=" ")
        i=i.next
    print()

def reverseLinkedList(head):
    stack=[]
    curr=head
    while curr!=None:
        stack.append(curr.key)
        curr=curr.next
    curr=head
    while curr!=None:
        curr.key=stack.pop()
        curr=curr.next
    return head    
print("Previous List:")
printList(head)
head=reverseLinkedList(head)
print("New List:")
printList(head)


"Efficient solution"


class Node:
    def __init__(self,k):
        self.key=k 
        self.next=None
head = Node(10)
head.next= Node(20)
head.next.next= Node(30)
head.next.next.next= Node(40)

def printList(head):
    i=head
    while i != None:
        print(i.key,end=" ")
        i=i.next
    print()

def reverseLinkedList(head):
    curr=head
    prev=None
    while curr !=None:
        next=curr.next
        curr.next=prev
        prev=curr
        curr=next
    return prev
print("Previous List:")
printList(head)
head=reverseLinkedList(head)
print("New List:")
printList(head)

