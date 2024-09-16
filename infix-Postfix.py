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

# Function to convert infix to postfix
def infixToPostfix(expression):
    # Stack for storing operators
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
            while (stack and precedence(char) <= precedence(stack[-1])) and isLeftAssociative(char):

                result.append(stack.pop())
            stack.append(char)

    # Pop all the operators left in the stack
    while stack:
        result.append(stack.pop())

    return ''.join(result)

# Test case
expression = "a+b*(c^d^e)^(f+g*h)-i"
print(infixToPostfix(expression))
