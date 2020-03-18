def sum(num1, num2):
    oper = num1 + num2
    return oper

def subtr(num1, num2):
    oper = num1 - num2
    return oper

def divis(num1, num2):
    oper = num1 // num2
    return oper

def multip(num1, num2):
    oper = num1 * num2
    return oper

try:
    number = int(input())
    operator = input()
    number2 = int(input())

    if operator == '+':
        print('=', sum(number, number2))
    elif operator == '-':
        print('=', subtr(number, number2))
    elif operator == '/':
        print('=', divis(number, number2))
    elif operator == '*':
        print('=', multip(number, number2))
except ValueError:
    print('Incorrect, please vyebi yourself in zheppu')