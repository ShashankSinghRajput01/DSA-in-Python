class Node:
    def __init__(self,k):
        self.key=k
        self.left=None
        self.right=None
    
def floorBST(root,x):
    res=None
    while root!=None:
        if root.key==x:
            return root.key
        elif root.key>x:
            root=root.left
        else:
            res=root
            root=root.right
    return res.key

root=Node(10)
root.left=Node(20)
root.right=Node(30)
root.right.left=Node(40)
root.right.right=Node(50)
print(floorBST(root,50))

