


t=int(input())

for _ in range(t):
    x,y=[int(x) for x in input().split()]

    if y%x!=0:
        print('0 0')
    else:
        print('%d %d'%(1,y//x))