

t=int(input())
for _ in range(t):
    a,b=[int(x) for x  in input().split()]


    if a<=b:
        print('10'*a+'1'*(b-a))
    else:
        print('01'*b+'0'*(a-b))