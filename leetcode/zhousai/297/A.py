class Solution:
    def calculateTax(self, brackets, income: int) -> float:

        ans=0
        n=len(brackets)
        pre=0
        for i in range(n):
            b,p=brackets[i]

            now=min(b,income)
            ans+=(now-pre)*p/100
            if b>=income:
                break
            pre=b

        return ans