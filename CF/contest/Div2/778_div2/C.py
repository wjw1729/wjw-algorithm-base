import heapq



t=int(input())
for _ in range(t):
    n=int(input())
    nums=[-int(x) for x in input().split()]
    heapq.heapify(nums)
    heap=[sum(nums)]


    while heap and nums and  heap[0]<=nums[0] :
        while nums and heap and  nums[0]==heap[0]:
            heapq.heappop(nums)
            heapq.heappop(heap)

        if heap:
            w0=heapq.heappop(heap)
            heapq.heappush(heap,w0//2)
            heapq.heappush(heap,w0//2 if w0%2==0 else w0//2+1)


    if not nums:
        print('YES')
    else:
        print('NO')






