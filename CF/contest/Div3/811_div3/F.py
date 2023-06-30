t=int(input())

for _ in range(t):
    n,d12,d23,d31=[int(x) for  x in input().split()]

    def solve():

        l=(d12+d31-d23)
        if l<0 or l%2!=0 :#
            print('NO')
            return
        l//=2

        #print(l)
        if d12-1+d31-l-1>n-3 or l>d12 or l>d31:
            print('NO')
            return


        if l==d31:
            ans=[]
            pre=1

            for i in range(4,4+d31-1):
                ans.append((pre,i))
                pre=i
            ans.append((pre,3))
            pre=3

            for i in range(4+d31-1,4+d31-1+d12-l-1):
                ans.append((pre,i))
                pre=i
            ans.append((pre,2))
            for i in range(4+d31-1+d12-l-1,n+1):
                ans.append((1,i))

            print('YES')
            for x in ans:
                print(*x)



        else:
            ans=[]
            pre=1
            node=1
            for i in range(4,4+d12-1):
                ans.append((pre,i))
                if i-4+1==l:
                    node=i
                pre=i

            if l==d12 :
                node=2

            ans.append((pre,2))

            pre=node
            for i in range(4+d12-1,4+d12-1+d31-l-1):
                ans.append((pre,i))

                pre=i

            ans.append((pre,3))

            for i in range(4+d12-1+d31-l-1,n+1):
                ans.append((1,i))

            print('YES')
            for x in ans:
                print(*x)


        return

    solve()











