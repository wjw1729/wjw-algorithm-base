

def minoperations(s):
    n=len(s)
    f=[0]*26
    ans=0
    for c in s:
        if f[ord(c)-ord('a')]:
            ans+=2
            f=[0]*26
        else:
            f[ord(c)-ord('a')]=1

    return n-ans

t=int(input())

for _ in range(t):
    s=input()
    print(minoperations(s))




