A = [0, 1, 2, 3, 4]
ind = int(input())

try:
    print(A[ind])
except IndexError:
    print('Don’t try buffer overflow attacks in Python!')