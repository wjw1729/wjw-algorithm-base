import itertools


class Solution:
    def readBinaryWatch(self, turnedOn: int):
        if turnedOn > 8:
            return []
        hours = ["0000", "0001", "0010", "0100", "1000", "0011", "0101", "0110", "1001", "1010", "0111","1011"]
        second = [[]] * 6

        for i in range(len(second)):
            a = ["1"] * i + ["0"] * (6 - i)
            b = list(set(itertools.permutations(a)))
            second[i] = ["".join(x) for x in b if int("".join(x), base=2) < 60]

        ans = []

        for i in range(len(hours)):

            hourcount = hours[i].count("1")

            if hourcount > turnedOn:
                break

            secondcount = turnedOn - hourcount
            for each_second in second[secondcount]:
                ans.append(str(int(hours[i], base=2)) + ":" + "{:02d}".format(int(each_second, base=2)))

        return ans


turnOn = 2
res = Solution().readBinaryWatch(turnOn)
print(res)
