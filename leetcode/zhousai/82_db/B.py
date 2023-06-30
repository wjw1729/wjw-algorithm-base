import bisect
class Solution:
    def latestTimeCatchTheBus(self, buses, passengers, capacity: int) -> int:
        buses.sort()
        n = len(buses)
        m = len(passengers)
        passengers.sort()


        pls=[]
        j=0
        for i in range(n):
            jj=j
            idx=bisect.bisect(passengers,buses[i])
            if idx-j>capacity:
                j=j+capacity
            else:
                j=idx
            pls.append(passengers[jj:j])



        ans=0
        idx=n-1
        sp=set()
        for p in pls:
            sp|=set(p)

        for p in pls[::-1]:

            if len(p)==capacity:
                for c in p[::-1]:
                    if c-1 not in sp:
                        return c-1
            else:
                if buses[idx] not in sp:
                    return buses[idx]
                for c in p[::-1]:
                    if c-1 not in sp:
                        return c-1


            idx-=1
        return  ans



buses = [18,8,3,12,9,2,7,13,20,5]

passengers = [13,10,8,4,12,14,18,19,5,2,30,34]

capacity = 1

res=Solution().latestTimeCatchTheBus(buses,passengers,capacity)
print(res)

