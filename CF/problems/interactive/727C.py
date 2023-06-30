


n=int(input())
ans=[0]*n

print('? 1 3',flush=True)
a=int(input())
print('? 2 3',flush=True)
b=int(input())
print('? 1 2',flush=True)
c=int(input())

ans[0]=(a+c-b)//2
ans[1]=c-ans[0]
ans[2]=a-ans[0]


for i in range(3,n):
    print('? 1',i+1,flush=True)


    ans[i]=int(input())-ans[0]




print('!',*ans,flush=True)
