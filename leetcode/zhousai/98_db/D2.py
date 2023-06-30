class segtree:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.tag = self.total = 0
        self._left = self._right = None

    @property
    def mid(self):
        return (self.start + self.end) // 2

    @property
    def left(self):
        self._left = self._left or segtree(self.start, self.mid)
        return self._left

    @property
    def right(self):
        self._right = self._right or segtree(self.mid + 1, self.end)
        return self._right

    def push0(self):
        self.left.total+=self.tag*(self.left.end-self.left.start+1)
        self.right.total+=self.tag*(self.right.end-self.right.start+1)
        self.left.tag+=self.tag
        self.right.tag+=self.tag
        self.tag=0


    def update0(self,l,r,val):
        if l<=self.start and self.end<=r:
            self.total+=(self.end-self.start+1)*val
            self.tag+=val
            return

        if self.tag!=0 and self.start!=self.end:
            self.push0()

        if l<=self.mid:
            self.left.update0(l,r,val)

        if r>self.mid:
            self.right.update0(l,r,val)

        self.total=self.left.total+self.right.total




    def push(self):
        self.left.total = self.left.end-self.left.start+1-self.left.total
        self.right.total = self.right.end - self.right.start + 1-self.right.total
        self.left.tag += self.tag
        self.right.tag += self.tag
        self.tag = 0

    def update(self, l, r):
        if l <= self.start and self.end <= r:
            self.total=(self.end-self.start+1)-self.total
            self.tag = 1
            return

        if self.tag != 0 and self.start != self.end:
            self.push()

        if l <= self.mid:
            self.left.update(l, r)

        if r > self.mid:
            self.right.update(l, r)

        self.total = self.left.total + self.right.total



    def query(self, l, r):
        if l <= self.start and self.end <= r:
            return self.total

        if self.tag != 0:
            self.push()

        res = 0
        if l <= self.mid:
            res += self.left.query(l, r)
        if r > self.mid:
            res += self.right.query(l, r)

        return res


class Solution:
    def handleQuery(self, nums1, nums2, queries):

        ans=[]
        s2=sum(nums2)
        s1=sum(nums1)
        print(s2)
        psum=0
        n=len(nums1)
        segt=segtree(0,n-1)
        for i in range(n):
            if nums1[i]==1:
                segt.update0(i,i,1)

        for q,l,r in queries:
            if q==1:
                s2+=s1*psum
                #print(s2)
                psum=0
                segt.update(l,r)
                s1=segt.query(0,n-1)
                #print(s1)


                #######
                nums1[l:r+1]=[1-x for x  in nums1[l:r+1]]
                print(sum(nums1),'#')
                #if sum(nums1)!=s1:
                tmp=[]
                #for i in range(n):
                    #tmp.append(segt.query(i,i))
                print(tmp,nums1)




            elif q==2:
                psum+=l

            else:
                s2+=s1*psum
                psum=0
                ans.append(s2)


        return ans

nums1 = [1,0,1]
nums2 = [0,0,0]
queries = [[1,1,1],[2,1,0],[3,0,0]]
nums1=[0,0,0,0,1,0,0,0,1,1,0,1,0,1,1,1,0,0,0,0,1,1,1]
nums2=[30,46,43,34,39,16,14,41,22,11,32,2,44,12,22,36,44,49,50,10,33,7,42]
queries=[[1,15,21],[3,0,0],[3,0,0],[2,21,0],[2,13,0],[3,0,0]]
nums1=[0,1,0,0,0,0]
nums2=[14,4,13,13,47,18]
queries=[[3,0,0],[1,4,4],[1,1,4],[1,3,4],[3,0,0],[2,5,0],[1,1,3],[2,16,0],[2,10,0],[3,0,0],[3,0,0],[2,6,0]]
res=Solution().handleQuery(nums1,nums2,queries)
print(res)