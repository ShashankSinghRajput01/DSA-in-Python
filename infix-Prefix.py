# Function to return precedence of operators
def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    if op == '^':
        return 3
    return 0

def isLeftAssociative(op):
    # '^' is right-associative, all others are left-associative
    if op == '^':
        return False
    return True

def revStr(expression):
    rev = ""
    for char in expression:
        if char == '(':
            rev += ')'
        elif char == ')':
            rev += '('
        else:
            rev += char
    return rev[::-1] 

# Function to convert infix to postfix
def infixToPrefix(expression):
    # Stack for storing operators
    expression=revStr(expression)

    stack = []
    # Result to store the postfix expression
    result = []

    # Traverse through each character in the infix expression
    for char in expression:
        # If the character is an operand (number or letter), add it to the result
        if char.isalnum():
            result.append(char)

        # If the character is '(', push it to the stack
        elif char == '(':
            stack.append(char)

        # If the character is ')', pop and output from the stack until '(' is found
        elif char == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()  # Remove '(' from the stack

        # If the character is an operator
        else:
            while (stack and precedence(char) < precedence(stack[-1])) or \
                (stack and precedence(char) == precedence(stack[-1]) and isLeftAssociative(char)):
                result.append(stack.pop())
            stack.append(char)

    # Pop all the operators left in the stack
    while stack:
        result.append(stack.pop())

    return ''.join(result[::-1])
    

# Test case
expression = "x+y*z"
print(infixToPrefix(expression))

