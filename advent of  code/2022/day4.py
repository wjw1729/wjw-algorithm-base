"""
ans=0
while 1:


    ip=input()
    if ip=='#':
        break
    sls=ip.split(',')
    a,b=sls[0].split('-')
    c,d=sls[1].split('-')
    a=int(a)
    b=int(b)
    c=int(c)
    d=int(d)
    if (a<=c and b>=d) or (a>=c and b<=d):
        ans+=1

print(ans)
"""







ans=0
while 1:


    ip=input()
    if ip=='#':
        break
    sls=ip.split(',')
    a,b=sls[0].split('-')
    c,d=sls[1].split('-')
    a=int(a)
    b=int(b)
    c=int(c)
    d=int(d)

    l=max(a,c)
    r=min(b,d)
    if l<=r:
        ans+=1

print(ans)
