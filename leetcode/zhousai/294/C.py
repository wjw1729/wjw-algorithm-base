class Solution:
    def minimumLines(self, stockPrices):

        stockPrices.sort()

        n=len(stockPrices)
        ans=1

        for i in range(2,n):
            if (stockPrices[i][1]-stockPrices[i-1][1])*(stockPrices[i-1][0]-stockPrices[i-2][0])==(stockPrices[i-1][1]-stockPrices[i-2][1])*(stockPrices[i][0]-stockPrices[i-1][0]):
                continue
            else:
                ans+=1


        return ans
