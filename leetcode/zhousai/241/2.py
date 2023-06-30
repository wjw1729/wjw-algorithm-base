"""
author:wjw
分析：
"""

class Solution:
    def minSwaps(self, s: str) -> int:
        n = len(s)
        if n % 2 == 1:
            if s.count('1') != n // 2 and s.count('1') != n // 2 + 1:
                return -1
        else:
            if s.count('1') != n // 2:
                return -1

        s1 = s[::2]
        s2=s[1::2]
        print(len(s1))
        num1 = s1.count('1')
        num0 = s1.count('0')
        num1_=s2.count('1')
        num0_=s2.count('0')
        return min(num1, num0)


s="00011110110110000000000110110101011101111011111101010010010000000000000001101101010010001011110000001101111111110000110101101101001011000011111011101101100110011111110001100110001110000000001100010111110100111001001111100001000110101111010011001"
res=Solution().minSwaps(s)
print(res)