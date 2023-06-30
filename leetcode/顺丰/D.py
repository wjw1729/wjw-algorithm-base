class Solution:
    def isPointInPolygon(self, x: float, y: float, coords ) -> bool:

        n=len(coords)
        pls=[]
        for i in range(0,n,2):
            x1,y1=coords[i:i+2]
            pls.append((x1,y1))

        def online(x0, y0, x1, y1, x2, y2):

            return (x1 - x0) * (y2 - y1) == (x2 - x1) * (y1 - y0) and (x0<=max(x1,x2) and x0>=min(x1,x2))

        def crossproduct(p, r, q):
            a = (q[0] - p[0], q[1] - p[1])
            b = (r[0] - p[0], r[1] - p[1])
            return a[0] * b[1] - a[1] * b[0]


        for i in range(1,n//2):
            tmp=crossproduct((x,y),pls[i],pls[i-1])
            if tmp<0 or (tmp==0 and online(x,y,*pls[i],*pls[i-1])):
                return False


        return True




x=6
y=3
coords=[1,2,3,4,5,3,6,1,3,1,1,2]
x=3
y=9
coords=[2,4,3,9,6,5,7,3,5,1,2,4]
x=78
y=92
coords=[111,88,140,121,179,130,190,177,71,119,1,22,111,88]

res=Solution().isPointInPolygon(x,y,coords)
print(res)

