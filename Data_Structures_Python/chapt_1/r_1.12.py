import random as ran

A = [1, 2, 4, 8, 16, 32, 64, 128, 256]
rannum = ran.choice(A)
rannum2 = ran.randrange(A[0], A[-1])

print(rannum, rannum2)