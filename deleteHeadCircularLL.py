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

def DelBegCircularLL(head):
    if head==None or head.next==head:
        return None
    curr=head
    while curr.next != head:
        curr=curr.next
    curr.next=head.next
    return curr.next

print("Previous List:")
printCircularList(head)
head=DelBegCircularLL(head)
print("\nNew List:")
printCircularList(head)

"OR OR OR Efficient sol"

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

def DelBegCircularLL(head):
    if head==None or head.next==head:
        return None
    else:
        head.key=head.next.key
        head.next=head.next.next
        return head


print("\nPrevious List:")
printCircularList(head)
head=DelBegCircularLL(head)
print("\nNew List:")
printCircularList(head)
