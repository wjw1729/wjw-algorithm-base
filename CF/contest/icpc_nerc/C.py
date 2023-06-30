


def connectthep(pointsls):


    ans=float('inf')
    path=[]




    def get(pointls):
        pointsls.sort(key=lambda x: x[0])
        ans=0
        x0,y0=pointls[0]
        x1, y1 = pointls[1]
        x2, y2 = pointls[2]

        path=[]

        if (y0-y1) *  (y1-y2)>=0:

            if abs(x1-x0)>0:
                path.append((x0,y0,x1,y0))
                ans+=abs(x1-x0)
            if abs(y1-y0)>0:
                path.append((x1,y0,x1,y1))
                ans+=abs(y1-y0)
            if abs(x2-x1)>0:
                path.append((x1,y1,x2,y1))
                ans+=abs(x2-x1)

            if abs(y2-y1)>0:
                path.append((x2,y1,x2,y2))
                ans+=abs(y2-y1)
        else:
            ans+=x1-x0
            path.append((x0,y0,x1,y0))


            yd=min(y0,y1,y2)
            yu=max(y0,y1,y2)
            ans+=yu-yd
            path.append((x1,yd,x1,yu))


            ans+=x2-x1
            path.append((x1,y2,x2,y2))


        return ans,path

    if len(set(x[0] for x in pointsls))==1:
        pointsls.sort(key=lambda x:x[1])
        return (pointsls[0][0],pointsls[0][1],pointsls[1][0],pointsls[1][1]),(pointsls[1][0],pointsls[1][1],pointsls[2][0],pointsls[2][1])

    if len(set(x[1] for x in pointsls))==1:
        pointsls.sort(key=lambda x: x[0])
        return (pointsls[0][0], pointsls[0][1], pointsls[1][0], pointsls[1][1]), (
        pointsls[1][0], pointsls[1][1], pointsls[2][0], pointsls[2][1])



    res,path1=get(pointsls)
    if res<ans:
        path=path1[:]
        ans=res

    pointsls=[(y,x) for x,y in pointsls]
    res,path2=get(pointsls)
    if res<ans:
        path=[(y1,x1,y2,x2)   for x1,y1,x2,y2 in path2]


    return path


pointls=[]
for i in range(3):
    pointls.append([int(x) for x  in input().split()])


res=connectthep(pointls)
print(len(res))
for x in res:
    print(' '.join([str(y) for y in  x]))




















