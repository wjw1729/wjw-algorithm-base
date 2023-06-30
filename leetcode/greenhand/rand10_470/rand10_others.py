"""
author:wjw
分析：
"""

import random
def rand7():
    return random.randint(1,7)

class Solution:
    def rand10(self):

        num=(rand7()-1)*7+rand7()

        while num>40:
            num=(rand7()-1)*7+rand7()

        return num%10+1


