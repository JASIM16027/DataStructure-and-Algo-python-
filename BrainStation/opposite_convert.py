t = int(input())
while t:
    s = input()
    d = {}
    cnt = 0
    cnt1 = 0
    f=1
    for i in range(len(s)):

        if s[i]=='a':
            if f==1:
                cnt+=1
        if s[i]=='b':
            if cnt>1 or cnt==0:
                cnt1+=1
            f = 0
    if cnt>1 and cnt1>1 or (cnt>1 and cnt==0) or (cnt>1 and cnt1==0):
        print('YES')
    else:
        print('NO')

    t-=1

