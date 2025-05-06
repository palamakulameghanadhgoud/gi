def evaluate_postfix(expression):
    stack = []
    operators = {'+', '-', '*', '/', '%', '^'}
    
    for token in expression.split():
        if token.isdigit():
            stack.append(int(token))
        elif token in operators:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a / b)  
            elif token == '^':
                stack.append(a**b)
            elif token == '%':
                stack.append(a%b)
    
    return stack.pop()

postfix_expr = input("Enter the postfix expression")
print("Post fix Expression = ",postfix_expr)
result = evaluate_postfix(postfix_expr)
print("Result:", result)
