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

def insertLinkedList(head,key):
    temp= Node(key)
    temp.next=head
    return temp
print("Previous List:")
printList(head)
head=insertLinkedList(head,5)
print("New List:")
printList(head)

    