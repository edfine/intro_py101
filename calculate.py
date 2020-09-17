import sys

def calculate(operand1, operand2, operator, **kwargs):
    useFloat = False
    
    if kwargs.get('float') == True: 
        operand1 = float(operand1)
        operand2 = float(operand2)
        useFloat = True
    else:
        operand1 = int(operand1)
        operand2 = int(operand2)

    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '/':
        if useFloat:
             return operand1 / operand2
        else:
            return operand1 // operand2

print("hello I'm in the calculate module")

for idx, arg in enumerate(sys.argv):
    print("arg %d is %s" % (idx, arg))