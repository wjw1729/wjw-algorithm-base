
t=int(input())

for _ in range(t):
    a,b,c,d=[int(x) for x  in input().split()]

    if a*d==b*c:
        print(0)
    elif a*d==0 or b*c==0 or a*d%(b*c)==0 or (b*c)%(a*d)==0:
        print(1)
    else:
        print(2)