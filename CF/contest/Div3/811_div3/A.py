

t=int(input())

for _ in range(t):
    n,H,M=[int(x) for  x in input().split()]
    ans=[24,0]
    for _ in range(n):
        h,m=[int(x) for  x in input().split()]

        def get(h1,m1,h2,m2):


            if m2>=m1:
                tmpm=m2-m1
            else:
                tmpm=m2-m1+60
                h2-=1

            if h2>=h1:
                tmph=h2-h1
            else:
                tmph=h2-h1+24

            return tmph,tmpm

        tmp=get(H,M,h,m)
        if tmp[0]*60+tmp[1]<ans[0]*60+ans[1]:
            ans=tmp


    print(*ans)

