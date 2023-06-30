class Solution:
    def countCombinations(self, pieces, positions):

        def  h_v_nums(position):
            x,y=position

            ans=[(x,i) for i in range(1,9)]
            ans+=[(i,y) for i in range(1,9) if i!=x]

            return ans


        def diag(position):
            x,y=position

            ans=[(i,x+y-i) for i in range(1,9) if 1<=(x+y-i)<9]
            ans+=[(i,i+y-x) for i in range(1,9) if 1<=(i+y-x)<9 and i!=x]

            return ans

        




