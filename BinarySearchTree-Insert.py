"Recursive"
class Node:
    def __init__(self,k):
        self.key=k
        self.left=None
        self.right=None

def insertBST(root,key):
    if root==None:
        return Node(key)
    elif root.key==key:
        return root
    elif root.key>key:
        root.left=insertBST(root.left,key)
    else:
        root.right=insertBST(root.right,key)
    return root
    
    
root=None
root=insertBST(root,10)
root=insertBST(root,15)
root=insertBST(root,20)
root=insertBST(root,5)

"Iteration Implementation"

class Node:
    def __init__(self,k):
        self.key=k
        self.left=None
        self.right=None

def itrinsertBST(root,key):
    parent=None
    curr=root
    while root!=None:
        parent=curr
        if curr.key==key:
            return True
        elif curr.key>key:
            root=root.left
        else:
            root=root.right
    if parent==None:
        return Node(key)
    if parent.key>key:
        parent.left=Node(key)
    else:
        parent.right=Node(key)
    return root

root=None
root=itrinsertBST(root,10)
root=itrinsertBST(root,12)
root=itrinsertBST(root,8)
    

    

