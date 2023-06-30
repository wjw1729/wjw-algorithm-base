

class Solution:
    def splitPainting(self, segments):
        ans=[]

        segments.sort(key=lambda x:(x[0],x[1]))
        n=len(segments)
        left=segments[0][0]
        right=segments[0][1]

        for i in range(n):



