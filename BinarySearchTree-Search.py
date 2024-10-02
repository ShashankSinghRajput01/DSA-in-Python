"Recursive Implementation"
class Node:
    def __init__(self,k):
        self.key=k
        self.left=None
        self.right=None
    
def searchBST(root,key):
    if root ==None:
        return False
    elif root.key==key:
        return True
    elif root.key>key:
        return searchBST(root.left,key)
    else:
        return searchBST(root.right,key)
    
root=Node(10)
root.left=Node(5)
root.right=Node(30)
root.right.left=Node(20)
root.right.right=Node(50)
key=40
print(searchBST(root,key))


"Iteration Implementation"

class Node:
    def __init__(self,k):
        self.key=k
        self.left=None
        self.right=None

def itrsearchBST(root,key):
    while root!=None:
        if root.key==key:
            return True
        elif root.key>key:
            root=root.left
        else:
            root=root.right
    return False
    
root=Node(10)
root.left=Node(5)
root.right=Node(30)
root.right.left=Node(20)
root.right.right=Node(50)
key=20
print(itrsearchBST(root,key))
