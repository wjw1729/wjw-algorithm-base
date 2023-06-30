

def printcards(r,c):

    print('..'+'+-'*(c-1)+'+')

    for i in range(r):
        s=''
        if i==0:
            s+='.'
        else:
            s+='|'
        for j in range(c):
            s+='.'
            s+='|'
        print(s)
        print('+-' * c+'+')




n=int(input())

for i in range(n):
    print('Case #%d:'%(i+1))
    r,c=[int(x) for x in input().strip().split()]
    printcards(r,c)




