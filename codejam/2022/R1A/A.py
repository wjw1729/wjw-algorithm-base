
def process(s):
    n=len(s)
    ans=''
    l=0
    while l<n:
        r=l+1
        while r<n and s[r]==s[r-1]:
            r+=1

        if r<n and ord(s[r])>ord(s[l]):
            ans+=s[l:r]*2
        else:
            ans+=s[l:r]
        l=r


    return ans



t=int(input())
for i in range(t):
    s=input()
    print('Case #%d: %s'%(i+1,process(s)))


