"""
author：wjw
分析：修订号依次比较即可！
"""


class Solution:
    def compareVersion(self, version1, version2):
        version1 = version1.split('.')
        version2 = version2.split('.')

        length = min(len(version1), len(version2))
        for i in range(length):

            if int(version1[i]) > int(version2[i]):
                return 1
            if int(version1[i]) < int(version2[i]):
                return -1

        if len(version1) > len(version2):
            s = ''
            for j in range(i + 1, len(version1)):
                s += version1[j]

            return int(int(s) > 0)

        if len(version1) < len(version2):
            s = ''
            for j in range(i + 1, len(version2)):
                s += version2[j]

            return -int(int(s) > 0)

        return 0
