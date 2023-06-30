print(1)
n=200000
print(n)
arr=[]
mask=(1<<17)-1
fill=int((1<<15)*1.3+1)


arr+=[mask+2]*2
x=6
for i in range(1,fill):
    arr+=[x]*2
    x=x*5+1
    x=x&mask

arr+=[1]*(n-len(arr))

s=' '.join(map(str,arr))
print(s)