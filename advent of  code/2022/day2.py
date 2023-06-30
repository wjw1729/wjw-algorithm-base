
"""
ans=0
while 1:
    ip=input()

    if ip=='#':
        break

    if ip[2]=='X':
        ans+=1
    elif ip[2]=='Y':
        ans+=2
    else:
        ans+=3



    if ord(ip[0])-ord('A')==ord(ip[2])-ord('X'):
        ans+=3
    elif (ip[0]=='A' and ip[2]=='Y') or (ip[0]=='B' and ip[2]=='Z') or (ip[0]=='C' and ip[2]=='X'):
        ans+=6

print(ans)
"""

ans=0
while 1:
    ip=input()
    if ip=='#':
        break

    if ip[2]=='X':
        if ip[0]=='A':
            ans+=3
        elif ip[0]=='B':
            ans+=1
        else:
            ans+=2


    elif ip[2]=='Y':
        ans+=3
        if ip[0]=='A':
            ans+=1
        elif ip[0]=='B':
            ans+=2
        else:
            ans+=3


    else:
        ans+=6
        if ip[0]=='A':
            ans+=2

        elif ip[0]=='B':
            ans+=3
        else:
            ans+=1



print(ans)


