# Function to evaluate a postfix expression
def evaluatePrefix(expression):
    # Stack to store operands
    stack = []
    chars = reversed(expression.split())

    # Traverse through each character in the postfix expression
    for char in chars:
        # If the character is an operand, push it to the stack
        if char.isdigit():
            stack.append(int(char))

        # If the character is an operator, pop two operands from the stack, apply the operator and push the result
        else:
            # Pop the top two operands from the stack
            val2 = stack.pop()
            val1 = stack.pop()

            # Perform the operation based on the operator
            if char == '+':
                stack.append(val2 + val1)
            elif char == '-':
                stack.append(val2 - val1)
            elif char == '*':
                stack.append(val2 * val1)
            elif char == '/':
                stack.append(int(val2 / val1))  # Perform integer division
            elif char == '^':
                stack.append(val2 ** val1)

    # The final value in the stack is the result of the expression
    return stack.pop()

# Test case
prefix_expression = "^ 10 ^ 2 3"
print(evaluatePrefix(prefix_expression))
