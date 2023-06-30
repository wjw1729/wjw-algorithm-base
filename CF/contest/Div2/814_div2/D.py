#本质上是求取不连续区间异或值为0的最大个数

t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]


    def solve():

        ans = n
        tp = 0
        st=set()
        st.add(0)

        for i in range(n):
            tp ^= a[i]
            if tp in st:
                ans -= 1
                st.clear()
            st.add(tp)

        print(ans)


    solve()
