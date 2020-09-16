def calculate(op1, op2, oper):
    op1 = float(op1)
    op2 = float(op2)
    
    if oper not in '+-*/':
        print('bad operator:', oper)
        return None
    
    if oper == '+':
        return op1 + op2
    if oper == '-':
        return op1 - op2
    if oper == '*':
        return op1 * op2
    if oper == '/':
        return op1 / op2

print(calculate(3, 4, '*'))