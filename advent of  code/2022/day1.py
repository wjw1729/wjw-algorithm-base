
ans=[0]*3
tmp=0




i=0
while 1:
    ip = input()

    if ip=='#':
        break
    if ip.isdigit():
        tmp+=int(ip)
    else:
        if tmp>=ans[0]:
            ans[0],ans[1],ans[2]=tmp,ans[0],ans[1]
        elif tmp>=ans[1]:
            ans[1],ans[2]=tmp,ans[1]
        elif tmp>ans[2]:
            ans[2]=tmp



        tmp=0
    i+=1

print(sum(ans))
