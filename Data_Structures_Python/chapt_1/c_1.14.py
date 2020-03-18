dig = input()
numb_dig = []
for a in dig.split():
    numb_dig.append(int(a))

prod_dig = []

for i in range(len(numb_dig)):
    for j in range(len(numb_dig)):
        if numb_dig[i] != numb_dig[j]:
            temp = numb_dig[i] * numb_dig[j]
            if temp % 2 == 1:
                prod_dig.append(temp)

print(prod_dig)