n = int(input())
summ = 0

def exers_6(m, j):
    if m > 0:
        for i in range(m):
            if m % 2 == 1:
                j += m**2
                m -= 1
            else:
                m -= 1
    return(j)

# summ = exers_6(n, summ)
A = [k**2 for k in range(1, (n+2)//2, 2*k-1)]

print(summ, sum(A))