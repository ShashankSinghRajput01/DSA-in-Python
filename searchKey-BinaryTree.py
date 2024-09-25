
class Node:
    def __init__(self,k):
        self.key=k
        self.left=None
        self.right=None
    
def searchKey(root,key):
    if root is None:
        return False
    elif root.key==key:
        return True
    elif searchKey(root.left,key)==True:
        return True
    else:
        return searchKey(root.right,key)
    
root=Node(10)
root.left=Node(60)
root.right=Node(30)
root.right.left=Node(40)
root.right.right=Node(50)
key=50
print(searchKey(root,key))
