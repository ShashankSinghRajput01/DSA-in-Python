"Using dictionary"
def isBalanced(s):
    stack=[]
    bracket_map={')': '(', '}': '{', ']': '['}
    for char in s:
        if char in bracket_map:
            top_element = stack.pop() 
            if bracket_map[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack
print(isBalanced("([[]])"))


"Efficient sol:"

def isBalanced(s):
    stack=[]
    for x in s:
        if x in "({[":
            stack.append(x)
        else:
            if not stack:
                return False
            elif isMatching(stack[-1],x)==False:
                return False
            else:
                stack.pop()
    if stack:
        return False
    else:
        return True

def isMatching(a,b):
    if (a=='(' and b==')') or (a=='{' and b=='}') or (a=='[' and b==']'):
        return True
    else:
        False
    
print(isBalanced("([[]])"))
    


