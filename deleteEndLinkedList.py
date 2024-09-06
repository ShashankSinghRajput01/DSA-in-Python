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

def deleteEndLinkedList(head):
    if head==None:
        return None
    if head.next==None:
        return None
    curr=head
    while curr.next.next!=None:
        curr=curr.next
    curr.next=None
    return head
    
print("Previous List:")
printList(head)
head=deleteEndLinkedList(head)
print("New List:")
printList(head)
