p = [1,2,3]
res = [[]]
for i in p:
    res += [j+[i] for j in res]
print(res)