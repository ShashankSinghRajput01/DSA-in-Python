class Node:
    def __init__(self,k):
        self.key=k
        self.left=None
        self.right=None
    
def ceilBST(root,x):
    res=None
    while root!=None:
        if root.key==x:
            return root.key
        elif root.key>x:
            res=root
            root=root.left
        else:
            root=root.right        
    return res.key

root=Node(20)
root.left=Node(10)
root.right=Node(30)
root.right.left=Node(25)
root.right.right=Node(50)
print(ceilBST(root,30))

