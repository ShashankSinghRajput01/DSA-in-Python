
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


def reverseDLL(head):
    if head==None :
        return None
    if head.next==None:
        return head
    curr=head
    prev=None
    while curr!=None:
        prev=curr
        curr.next,curr.prev=curr.prev,curr.next
        curr=curr.prev
    return prev
print("\nPrevious List:")  
printList(head)
head=reverseDLL(head)
print("\nNew List:")
printList(head)


