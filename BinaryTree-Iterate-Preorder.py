class Node:
    def __init__(self,k):
        self.key=k
        self.left=None
        self.right=None
    
def itrPreorder(root):
    if root is None:
        return
    st=[root]
    while len(st)>0:
        curr=st.pop()
        print(curr.key,end=" ")
        if curr.right is not None:
            st.append(curr.right)
        if curr.left is not None:
            st.append(curr.left)
    

root=Node(10)
root.left=Node(20)
root.right=Node(30)
root.right.left=Node(40)
root.right.right=Node(50)
itrPreorder(root)


    