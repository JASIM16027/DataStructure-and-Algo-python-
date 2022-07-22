"""
from collections import Counter
Mylist = [1, 2, 3, 4, 5, 2, 3, 4, 5]
d = dict(Counter(Mylist))
print(d)

ml = {i: Mylist.count(i) for i in Mylist}
print(ml)



Mylist = [1, 2, 3, 4, 5, 2, 3, 4, 5]
counter = {}

for i in Mylist:
    if not i in counter:
        counter[i] = 1
    else:
        counter[i] += 1

print(counter)

"""
"""
a = [4, 4, 1, 2, 3, 1, 2, 3]

dic = {}
for i in a:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] = dic[i]+1
print(dic)
j = 1
for i in dic:
    if dic[i]>1:
        print('{} {}'.format(i, j))
        j+=1
"""
"""
s = 'ifailuhkqq'
a = []

for i in range(len(s)):
    b = []

    for j in range(i + 1):
        b.append(s[j])
    a.append(''.join(b))
print(a)
c = []
for i in range(len(s)-1, -1, -1):
    d = []
    for j in range(len(s)-1,i-1,-1):

            d.append(s[j])
    c.append(''.join(d))

print(c)
cnt = 0
for i in range(len(s)):
    if a[i] == c[i]:
        cnt+=1
print(cnt)
cdcd
abba
abcd

"""

s = 'cdcd'
a = []
cnt = 0
for k in range(len(s)):

    for i in range(k, len(s)):
        b = []

        for j in range(k, i+1):
            b.append(s[j])
        a.append(''.join(b))
print(a)

for i in range(len(a)):
    for j in range(i+1, len(a)):

            if a[i] == a[j]:
                print(a[i])
                cnt+=1
c =[]
for i in range(len(s)-1, -1, -1):
    d = []
    for j in range(len(s)-1,i-1,-1):

            d.append(s[j])
    c.append(''.join(d))

print(c)