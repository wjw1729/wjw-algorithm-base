"""
author:wjw
分析：贪心。设a，b从index1,index2两个下标处进行选择。有两套方案：c1=a[index1]-b[index2],c2=a[index2]-b[index1].比较c1和c2哪个为最优策略.
    c1-c2=(a[index1]+b[index1])-(a[index2]+b[index2])>0,则a选择index1.否则选择index2。
    所以推广到n项也是一样的.a优先选择a[i]+b[i]中值大的index.

    a的选择策略确定了之后，就是求在此策略下的a的值。再求b的值。则最后两者的大小决定了谁获得胜利。
"""


class Solution:
    def stoneGameVI(self, aliceValues, bobValues):
        n = len(aliceValues)
        stones = [aliceValues[i] + bobValues[i] for i in range(n)]

        stones = list(enumerate(stones))
        stones.sort(key=lambda x: x[1], reverse=True)

        tmp1 = sum([aliceValues[stones[i][0]] for i in range(len(stones)) if i % 2 == 0])
        tmp2 = sum([bobValues[stones[i][0]] for i in range(len(stones)) if i % 2 == 1])
        if tmp1 > tmp2:
            return 1
        elif tmp1 == tmp2:
            return 0
        else:
            return -1


aliceValues = [1, 3]
bobValues = [2, 1]
aliceValues = [1, 2]
bobValues = [3, 1]
aliceValues = [2, 9, 1, 1, 1, 3, 5, 8, 8, 6, 8, 6, 2, 4]
bobValues = [1, 9, 7, 8, 3, 4, 2, 7, 8, 10, 1, 7, 10, 4]
res = Solution().stoneGameVI(aliceValues, bobValues)
print(res)
