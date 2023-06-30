class Solution:
    def ringGame(self, challenge) -> int:
        l = min(challenge)
        r = max(challenge)

        n = len(challenge)

        def canPass(x):

            maxOsum = x
            for i, num in enumerate(challenge):
                if num <= x and num | x >= maxOsum:
                    idx = i
                    maxOsum = num | x

            l = idx - 1
            r = idx + 1

            grades = maxOsum

            while l != r:
                if grades >= challenge[l]:
                    grades = max(grades, grades | challenge[l])
                    l = (l - 1 + n) % n
                if grades >= challenge[r]:
                    grades = max(grades, grades | challenge[r])
                    r = (r + 1) % n
                if grades < challenge[l] and grades < challenge[r]:
                    break

            return l == r

        return canPass(4)


challenge = [5, 4, 6, 2, 7]
res = Solution().ringGame(challenge)
print(res)
