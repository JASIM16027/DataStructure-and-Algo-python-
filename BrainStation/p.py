"""
n, m = map(int, input().split(" "))
ll = list(map(int, input().split(" ")))
arr = sorted(ll)
print(arr[-m])
"""
"""
t = int(input())
while t:
    n = int(input())
    ll = list(map(int, input().split(" ")))
    flag = 1
    for i in range(n - 1):
        if ll[i] > ll[i + 1]:
            flag = 0
            break
    if flag:
        print("Yes")
    else:
        print("No")
    t -= 1


t = int(input())
while t:
    x = list(map(int, input().split(" ")))
    n, m = x[0], x[1]
    ll = list(map(int, input().split(" ")))
    l, r = 0, 0
    sm = 0
    cnt = 0
    while l < n:
        if r < n and (sm + ll[r]) < m:
            sm += ll[r]
            r += 1
        else:
            cnt += (r - l)
            sm -= ll[l]
            l += 1

    print(cnt)
    t -= 1
"""
"""s = "deeedbbcccbdaa"
k = 3
stack = []

for i in s:
    if stack and stack[-1][0] == i:
        stack[-1][1] += 1
    else:
        stack.append([i, 1])
    if stack[-1][1] == k:
        stack.pop()
output = ""
for i, cnt in stack:
    output += i * cnt
print(output)
"""
nums = [100, 80, 60, 70, 60, 75, 85]
stack = []
res = []
for i in range(len(nums)):
    if not stack:
        res.append(-1)

    elif stack and stack[-1][0]>nums[i]:
        res.append(stack[-1][-1])
    elif stack and stack[-1][0]<=nums[i]:
        while stack and stack[-1][0]<=nums[i]:
            stack.pop()
        if not stack:
            res.append(-1)
        else:
            res.append(stack[-1][-1])

    stack.append((nums[i],i))
final_res = []
for i,v in enumerate(nums):
    final_res.append(i-res[i])

print(final_res)