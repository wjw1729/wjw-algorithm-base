"""
author:wjw
输入：nums=[10,9,500,35]，
输出：最大数的组合
分析：元素中首位大的放前面，然后比较次位，依次进行，若次位为none，则为最大（放前面）,相等——>末尾填充
"""


def judge(num1,num2):
    """
    以分析中的规则判断二者的大小
    :param num1: 
    :param num2: 
    :return: bool value，True表示num1>num2;Fasle:表示相反
    """""

    if int(str(num1)+str(num2))>int(str(num2)+str(num1)):
        return True
    else:
        return False


class Solution(object):
    def largestNumber(self,nums):
        """

        :param nums:List[int]
        :return:str
        """
        if len(nums)<2:
            return nums

        else:
            pivot=nums[0]
            less=[i for i in nums[1:] if judge(i,pivot)==False]
            more=[i for i in nums[1:] if judge(i,pivot)==True]

            return self.largestNumber(more)+[pivot]+self.largestNumber(less)


s=Solution()
x=s.largestNumber([0,0])
i=0
y=''
while i<len(x):
    y=y+str(x[i])
    i=i+1
if y=='00':
    y='0'
print(y)