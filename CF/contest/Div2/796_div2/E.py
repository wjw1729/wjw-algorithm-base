

n,m=[int(x) for x in input().split()]
edges=[]
for i in range(m):
    print('? '+'0'*i +'1'+'0'*(m-1-i),flush=True)
    edges.append((i,int(input())))


edges.sort(key=lambda x:x[1])


s=['0']*m
f=[0]*(m+1)

for i in range(m):
    s[edges[i][0]]='1'
    print('? '+''.join(s),flush=True)
    f[i+1]=int(input())

ans=0
for i in range(1,m+1):
    if f[i]==f[i-1]+edges[i-1][1]:
        ans+=edges[i-1][1]

print('!',ans,flush=True)



