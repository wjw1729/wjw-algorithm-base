"""

ans=0
while 1:
    ip=input()
    if ip=='#':
        break
    n=len(ip)
    s1=set(ip[:n//2])
    s2=set(ip[n//2:])
    tmp=s1&s2
    for a in tmp:
        if a.islower():
            ans+=ord(a)-ord('a')+1
        else:
            ans+=ord(a)-ord('A')+27




print(ans)

"""
ans=0
while 1:

    for i in range(3):
        ip=input()
        if ip=='#':
            break
        if i==0:
            res=set(ip)
        else:
            res&=set(ip)

    if ip=='#':
        break

    for a in res:
        if a.islower():
            ans += ord(a) - ord('a') + 1
        else:
            ans += ord(a) - ord('A') + 27

print(ans)