"Method 1 Using List"

print("\nUsing List:")
stack=[]
stack.append(10)
stack.append(20)
stack.append(30)
print(stack.pop())
top=stack[-1]
print(top)
size=len(stack)
print(size)
print("\nUsing Deque:")

"Method 2 Using Deque"

from collections import deque
stack=deque()
stack.append(10)
stack.append(20)
stack.append(30)
print(stack.pop())
top=stack[-1]
print(top)
size=len(stack)
print(size)