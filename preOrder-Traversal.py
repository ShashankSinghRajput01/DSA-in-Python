class Node:
    def __init__(self,k):
        self.key=k
        self.left=None
        self.right=None
    
def preorder(root):
    if root!=None:
        print(root.key,end=" ")
        preorder(root.left)
        preorder(root.right)

root=Node(10)
root.left=Node(20)
root.right=Node(30)
root.right.left=Node(40)
root.right.right=Node(50)
preorder(root)


    