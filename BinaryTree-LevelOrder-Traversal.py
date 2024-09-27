from collections import deque
class Node:
    def __init__(self,k):
        self.key=k
        self.left=None
        self.right=None
    
def printLevelOrder(root):
    if root is None:
        return
    q=deque()
    q.append(root)
    while len(q)>0:
        node=q.popleft()
        print(node.key,end=" ")
        if node.left is not None:
            q.append(node.left)  
        if node.right is not None:
            q.append(node.right) 

root=Node(10)
root.left=Node(20)
root.right=Node(30)
root.right.left=Node(40)
root.right.right=Node(50)
printLevelOrder(root)
