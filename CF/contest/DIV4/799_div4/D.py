
def trans(s):
    return int(s[:2])*60+int(s[3:])


t=int(input())
for _ in range(t):
    s,x=input().split()

    plins=['00:00','01:10','02:20','03:30','04:40','05:50',
           '10:01','11:11','12:21','13:31','14:41','15:51',
           '20:02','21:12','22:22','23:32']

    x=int(x)
    now=trans(s)
    ans=0
    for t in plins:
        ed=trans(t)
        if ed<now:
            ed+=1440
        dt=ed-now
        for k in range(1441):
            if (k*x-dt)%1440==0:

                ans+=1
                break

    print(ans)