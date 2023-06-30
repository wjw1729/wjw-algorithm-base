
def get_s(s):
    res=[]
    for i in range(n-1):
        res.append(int(s[i])^int(s[i+1]))

    return res



q=int(input())
for _ in range(q):
    n=int(input())
    s=input()
    t=input()

    s_=get_s(s)
    t_=get_s(t)

    if s_.count(1)!=t_.count(1) or s[0]!=t[0] or s[-1]!=t[-1]:
        print(-1)
    else:
        a=[i for i,c in enumerate(s_) if c==1]
        b=[i for i,c in enumerate(t_) if c==1]
        print(sum(abs(a[i]-b[i]) for i in range(len(a))))


