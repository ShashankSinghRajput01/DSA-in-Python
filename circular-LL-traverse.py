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
printCircularList(head)