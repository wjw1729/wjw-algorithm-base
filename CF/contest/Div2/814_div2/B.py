

t=int(input())
for _ in range(t):
    n,k=[int(x) for x in input().split()]

    def solve():
        if k%2==1:
            print('YES')
            for i in range(1,n,2):
                print(i,i+1)



        else:
            if k%4!=0:
                print('YES')

                odd=list(range(1,n,2))
                j=0
                for i in range(1,n+1):
                    if i%4==0:
                        print(odd[j],i)
                        j+=1
                    if (i+k)%4==0:
                        print(i,odd[j])
                        j+=1

            else:
                print('NO')
    solve()