
def redversusblue(a,b):
    if a==b:
        return 'Rb'*a

    if a>b:
        lsa=[a//(b+1)]*(b+1)
        for i in range(a%(b+1)):
            lsa[i]+=1

        res=''
        for i in range(b):
            res+='R'*lsa[i]
            res+='B'
        res+='R'*lsa[-1]

        return res

    if a<b:
        lsb=[b//(a+1)]*(a+1)
        for i in range(b%(a+1)):
            lsb[i]+=1

        res=''
        for i in range(a):
            res+='B'*lsb[i]
            res+='R'
        res+='B'*lsb[-1]
    return res

t=int(input())
for _ in range(t):
    _,a,b=[int(x) for x in input().split()]
    print(redversusblue(a,b))






