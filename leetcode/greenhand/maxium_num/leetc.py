class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        if set(nums) == 0:
            return '0'

        res_ls = quicksort(nums)
        res = ''
        i = 0
        while i < len(res_ls):
            res += str(res_ls[i])
            i = i + 1

        return res


def judge(num1, num2):
    """
    以分析中的规则判断二者的大小
    :param num1: 
    :param num2: 
    :return: bool value，True表示num1>num2;Fasle:表示相反
    """""

    if int(str(num1) + str(num2)) > int(str(num2) + str(num1)):
        return True
    else:
        return False


def quicksort(nums):
    if len(nums) < 2:
        return nums

    else:
        pivot = nums[0]
        less = [i for i in nums[1:] if judge(i, pivot) == False]
        more = [i for i in nums[1:] if judge(i, pivot) == True]

        return quicksort(more) + [pivot] + quicksort(less)

s=Solution()
s.largestNumber([0,0])