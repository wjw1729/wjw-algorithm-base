def gcd(a,b):
    return b if a%b==0 else gcd(b,a%b)


def shift(s):
    for i in range(1,len(s)+1):
        if s==s[i:]+s[:i]:
            return i

def solve():
    used=[False]*n
    ans=1
    i=0
    while i<n:
        ss=''
        while not used[i]:
            ss+=s[i]
            used[i]=True
            i=p[i]

        i+=1
        if len(ss)==0:
            continue
        ln=shift(ss)
        ans=ans*ln//gcd(ans,ln)

    return ans




t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    p = [int(x)-1 for x in input().split()]
    res=solve()

    print(res)






