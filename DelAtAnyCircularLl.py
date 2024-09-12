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

def DelAtAnyCircularLL(head,pos):
    if head==None :
        return None
    elif pos==1:
        if head.next==head:
            return head
        head.key=head.next.key
        head.next=head.next.next
        return head
    else:
        curr=head
        for i in range (pos-2):
            curr=curr.next
        curr.next=curr.next.next
        return head
print("\nPrevious List:")
printCircularList(head)
head=DelAtAnyCircularLL(head,2)
print("\nNew List:")
printCircularList(head)

