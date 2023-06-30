
n=int(input())
a=[int(x) for x in input().split()]
q=int(input())
b=[i+1-a[i] for i in range(n)]


preb=[0]*n
log=[0]*n
for i in range(1,n):

    preb[i]=max(preb[i-1],b[i])


ans=(n+1)*n//2


sb=[0]*(n+1)

for i in range(1,n+1):
    sb[i]=sb[i-1]+preb[i-1]


for _ in range(q):
    p,x=[int(x) for x in input().split()]
    res=ans-()


    def get(p,x):
        p=p-1
        if preb[p-1]>=p+1-a[p]:
            return sb[-1]
        ans=sb[-1]










