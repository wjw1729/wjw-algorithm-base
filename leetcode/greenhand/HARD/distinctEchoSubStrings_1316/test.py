class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:

        if denominator * numerator >= 0:
            sign = 1
        else:
            sign = -1

        print(sign)
        denominator = abs(denominator)
        numerator = abs(numerator)

        divisor = numerator // denominator
        remainder = numerator % denominator

        res = []
        res.append(divisor)
        hashindex = {}
        index = 0
        if remainder == 0:
            return str(divisor) if sign == 1 else '-' + str(divisor)

        preindex = -1
        while remainder != 0:
            index += 1
            if remainder in hashindex:
                preindex = hashindex[remainder]

                break
            hashindex[remainder] = index

            divisor = remainder * 10 // denominator
            remainder = remainder * 10 % denominator

            res.append(divisor)

        res = [str(x) for x in res]
        print(len(res))
        if preindex != -1:
            res.insert(preindex, '(')
        if len(res) > 1:
            res.insert(1, '.')
        if preindex != -1:
            res.append(')')

        return ''.join(res) if sign == 1 else '-' + ''.join(res)


numerator = -2147483648
denominator = 1
res = Solution().fractionToDecimal(numerator, denominator)
print(res)
