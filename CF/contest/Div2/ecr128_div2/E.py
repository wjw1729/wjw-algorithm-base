
def minmoves(b):
    f1=[0]*n
    f2=[0]*n
    f3=[0]*n

    if b[0].count('*')+b[1].count('*')==1:
        return 0


    for i in range(n-1,-1,-1):
        if b[0][i]=='*' or b[1][i]=='*':
            end=i
            break

    for i in range(n):
        if b[0][i]=='*' or b[1][i]=='*':
            s=i
    
            break
    if b[0][s]=='*' and b[1][s]=='*':
        f1[s],f2[s]=2,2
        f3[s]=2
    elif b[0][s]=='*':
        f1[s]=1
        f2[s]=2
        f3[s]=2
    elif b[1][s]=='*':
        f1[s]=2
        f2[s]=1
        f3[s]=2
    
    for i in range(s+1,end+1):

        if b[0][i]=='*' and b[1][i]=='*':
            f1[i]=min(f1[i - 1], f2[i - 1], f3[i - 1]) + 2
            f2[i] = min(f1[i - 1], f2[i - 1], f3[i - 1]) + 2
            f3[i] = min(f1[i - 1], f2[i - 1], f3[i - 1]) + 2
        elif  b[0][i]=='*' :
            f1[i] = min(f1[i - 1] + 1, f3[i - 1] + 1)
            f2[i] = min(f1[i - 1], f2[i - 1], f3[i - 1]) + 2
            f3[i] = min(f1[i - 1], f2[i - 1], f3[i - 1]) + 2

        elif  b[1][i]=='*':
            f1[i] = min(f1[i - 1], f2[i - 1], f3[i - 1]) + 2
            f2[i] = min(f2[i - 1] + 1, f3[i - 1] + 1)
            f3[i] = min(f1[i - 1], f2[i - 1], f3[i - 1]) + 2

        else:
            f1[i] = min(f1[i - 1] + 1, f3[i - 1] + 1)
            f2[i] = min(f2[i - 1] + 1, f3[i - 1] + 1)
            f3[i] = min(f1[i - 1], f2[i - 1], f3[i - 1]) + 2


    return min(f1[end],f2[end],f3[end])-1
            
            


t=int(input())

for _ in range(t):
    n=int(input())
    b=[]
    b.append(input())
    b.append(input())

    res=minmoves(b)
    print(res)