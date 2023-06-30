


from collections import Counter


class Solution:
    def halfQuestions(self, questions) -> int:
        n = len(questions) // 2
        d = Counter(questions)
        i=0
        for k, v in sorted(d.items(), key=lambda x: x[1], reverse=True):
            if n <= 0:
                break
            n -= v
            i += 1

        return i

questions = [2,1,6,2]
questions = [1,5,1,3,4,5,2,5,3,3,8,6]
res=Solution().halfQuestions(questions)
print(res)