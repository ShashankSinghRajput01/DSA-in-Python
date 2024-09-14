
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


def deleteHeadDLL(head,x):
    if head==None or head.next==None:
        return None
    else:
        head=head.next
        head.prev=None
        return head
    
print("\nPrevious List:")  
printList(head)
head=deleteHeadDLL(head,5)
print("\nNew List:")
printList(head)


