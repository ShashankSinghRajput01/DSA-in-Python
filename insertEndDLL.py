
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
    temp=Node(x)
    if head==None:
        return temp
    curr=head   
    while curr.next!=None:
        curr=curr.next
    curr.next=temp
    temp.prev=head
    return head
    
print("\nPrevious List:")  
printList(head)
head=insertBegDLL(head,5)
print("\nNew List:")
printList(head)


