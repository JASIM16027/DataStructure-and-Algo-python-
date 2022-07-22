nums = [1, 2, 3]
res = [[]]
for num in nums:
    res += [i+[num] for i in res]
print(res)
