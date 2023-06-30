

def minimumdays(heights):

    def solve(waters,days):
        num1=(days+1)//2
        num2=days//2

        if sum(waters)>num1+2*num2:
            return False
        for water in waters:
            d=water//2
            s=water%2

            if d<=num2:
                num2-=d
            else:
                num1-=2*(d-num2)
                num2 = 0
            num1-=s
            if num1<0 :
                return False
        return True

    ans=float('inf')
    maxh=max(heights)
    heights1=[maxh-x for  x in heights]
    heights2=[maxh-x+1 for x in heights]

    l = 0
    r =sum(heights2)//3*2+10**9


    while l<=r:
        mid=(l+r+1)//2
        if solve(heights1,mid):
            ans=min(ans,mid)
            r=mid-1
        else:
            l=mid+1

    l=0
    r=10**9
    while l<=r:
        mid=(l+r+1)//2
        if solve(heights2,mid):
            ans=min(ans,mid)
            r=mid-1
        else:
            l=mid+1

    return ans


t=int(input())

for _ in range(t):

    _=input()

    heights=[int(x) for x in input().strip().split()]

    print(minimumdays(heights))



