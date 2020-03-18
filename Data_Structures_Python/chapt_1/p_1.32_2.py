def sum(operat):
    oper = int(operat[0]) + int(operat[2])
    return oper

def subtr(operat):
    oper = int(operat[0]) - int(operat[2])
    return oper

def divis(operat):
    oper = int(operat[0]) // int(operat[2])
    return oper

def multip(operat):
    oper = int(operat[0]) * int(operat[2])
    return oper

try:
    operation = input()
    operation = operation.split()
    print(operation)

    if operation[1] == '+':
        print('=', sum(operation))
    elif operation[1] == '-':
        print('=', subtr(operation))
    elif operation[1] == '/':
        print('=', divis(operation))
    elif operation[1] == '*':
        print('=', multip(operation))
except ValueError:
    print('Incorrect, please vyebi yourself in zheppu')