


def canget(s,t):

    n=len(s)
    m=len(t)



    indices=[[] for _ in range(26)]

    for i in range(n):
        indices[ord(s[i])-ord('A')].append(i)

    pre=n
    for i in range(m-1,-1,-1):
        od=ord(t[i])-ord('A')
        if not indices[od]:
            return False
        idx=indices[od].pop()
        if idx>=pre:
            return False
        else:
            pre=idx
    return True


t=int(input())

for _ in range(t):
    s,t=input().split()
    if canget(s,t):
        print('YES')
    else:
        print('NO')
