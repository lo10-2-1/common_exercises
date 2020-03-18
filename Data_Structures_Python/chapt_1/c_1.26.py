a = int(input())
b = int(input())
c = int(input())

if a + b == c:
    print(a, '+', b, '=', c, sep=' ')
else:
    print('Incorrect:', a, '+', b, '=', c, sep=' ')

if b - c == a:
    print(b, '-', c, '=', a, sep=' ')
else:
    print('Incorrect:', b, '-', c, '=', a, sep=' ')

if a * b == c:
    print(a, '*', b, '=', c, sep=' ')
else:
    print('Incorrect:', a, '*', b, '=', c, sep=' ')