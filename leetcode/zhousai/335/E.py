class Solution:
    def findLongestSubarray(self, array) :

        n = len(array)


        maxl = 0
        ans = -1
        d = {}
        d[0] = 0
        pre = 0
        for i in range(1, n + 1):
            if array[i - 1].isalpha():
                pre += 1
            else:
                pre -= 1

            print(pre, i)
            if pre in d and maxl < i - d[pre]:
                maxl = i - d[pre]
                ans = i
                print(pre, i)

            if pre not in d:
                d[pre] = i

        print(d)
        if ans == -1:
            return []

        print(maxl)

        return array[ans-maxl:ans ]


array =["A", "1", "B", "C", "D", "2", "3", "4", "E", "5", "F", "G", "6", "7", "H", "I", "J", "K", "L", "M"]
res = Solution().findLongestSubarray(array)
print(res)
