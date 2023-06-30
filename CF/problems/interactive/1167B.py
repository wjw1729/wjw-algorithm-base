
a=[4 , 8, 15, 16, 23, 42]

d={}
for i in range(6):
    for j in range(i+1,6):
      d[a[i]*a[j]]=[a[i],a[j]]



ans=[0]*6
print('? 1 2',flush=True)
A=int(input())


print('? 2 3',flush=True)
B = int(input())


ans[1]=list(set(d[A]) & set(d[B]))[0]
ans[0]=list(set(d[A]) - set(d[B]))[0]
ans[2]=list( set(d[B])-set(d[A]))[0]

print('? 4 5',flush=True)
A=int(input()   )

print('? 5 6',flush=True)
B=int(input())

ans[4]=list(set(d[A]) &set(d[B]))[0]
ans[3]=list(set(d[A]) -set(d[B]))[0]
ans[5]=list(set(d[B])-set(d[A]))[0]


print('!',*ans,flush=True)








