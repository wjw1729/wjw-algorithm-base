


def promisingstring(s):
    n=len(s)

    presum=[0]*(n+1)
    ans=0


    for i in range(1,n+1):
        if s[i-1]=='+':
            presum[i]=presum[i-1]+1
        else:
            presum[i] = presum[i - 1] -1



    for i in range(1,n+1):
        for j in range(i):
            if presum[i]-presum[j]<=0 and (presum[i]-presum[j])%3==0:
                ans+=1

    return ans


t=int(input())

for _ in range(t):
    _=input()
    s=input()
    print(promisingstring(s))
