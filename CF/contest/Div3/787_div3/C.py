

def numbers(s):
    if len(s)==1:
        return 1

    n=len(s)
    pre=[0]*n

    for i in range(1,n):
        if s[i-1]=='0':
            pre[i]=pre[i-1]+1
        else:
            pre[i]=pre[i-1]


    suf=[0]*n

    for i in range(n-2,-1,-1):
        if s[i+1]=='1':
            suf[i]=suf[i+1]+1
        else:
            suf[i]=suf[i+1]
    ans=0
    for i in range(n):
        if pre[i]==suf[i]==0:
            ans+=1
    return ans



t=int(input())

for _ in range(t):
    s=input()
    ans=numbers(s)
    print(ans)