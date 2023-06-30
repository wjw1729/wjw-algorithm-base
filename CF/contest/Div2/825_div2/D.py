# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:

        node = head
        nums = set(nums)
        ans = 0
        while node:
            while node and node.val in in nums:
                node = node.next
            ans += 1
            if node:
                node = node.next

        return ans
