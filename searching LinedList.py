class Node:
    def __init__(self,k):
        self.key=k 
        self.next=None
head = Node(10)
head.next= Node(20)
head.next.next= Node(30)
head.next.next.next= Node(40)

def searchLinkedList(head,x):
    curr=head
    pos=1
    while curr != None:
        if curr.key==x: 
            return pos
        else:
            curr=curr.next
            pos=pos+1
    else:
        return -1
print (searchLinkedList(head,20) )   

    
        