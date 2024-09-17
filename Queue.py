"Method 1 Using Linked List"
q=[]
q.append(10)
q.append(20)
q.append(30)
print(q)
print(q.pop(0))
q.append(40)
print(q)
print(q.pop(0))
print(q)
print(len(q))
print(q[0])
print(q[-1])

"Method 2 using Import Deque"

from collections import deque
q=deque()
q.append(10)
q.append(20)
q.append(30)
print(q)
print(q.popleft())
q.append(40)
print(q.popleft())
print(len(q))
print(q[0])
print(q[-1])