def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2,'%':2, '^': 3}
    output = []
    stack = []
    
    for token in expression:
        if token.isalnum():  
            output.append(token)
        elif token in precedence:
            while stack:
                op_top = stack[-1]
                if op_top == '(' or precedence.get(op_top, 0) < precedence[token]:
                    break
                output.append(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
    
    while stack:
        output.append(stack.pop())
    
    return ''.join(output)

#infix_expr = "a+b*(c^d-e)^(f+g*h)-i"
infix_expr = input("Enter the infix expression")
print("Infix Expression = ",infix_expr)
postfix_expr = infix_to_postfix(infix_expr)
print("Postfix Expression:", postfix_expr)
