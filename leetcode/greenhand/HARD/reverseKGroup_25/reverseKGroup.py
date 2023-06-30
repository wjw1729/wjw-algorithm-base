"""
author；wjw
分析：用k维数组来存放反转链表。但是演技的保存下一次开始的结点以及上次反转之后的最后结点。在数组长度小于k时，提前结束。而且在最后一次未提前结束的翻转后，记得将最后出栈的结点连到None，避成环！
    next_node存放下一次开始反转的结点，pre_node存放上一次反转之后最后出栈的结点。pre用来存放反转过程中的上个结点。
"""


class Solution:
    def reverseKGroup(self, head, k):

        next_node = head

        temp = []
        i = 0
        while next_node:

            node = next_node
            while len(temp) < k and node != None:
                temp.append(node)
                node = node.next

            if len(temp) < k:
                pre_node.next = temp[0]
                break

            next_node = node

            # print(len(temp))
            pre = temp.pop()
            if i == 0:
                head = pre
            else:
                pre_node.next = pre
            node = pre
            while temp:
                node = temp.pop()
                pre.next = node
                pre = node
                # print(len(temp))
            pre_node = node

            if next_node == None:
                pre_node.next = None

            i += 1

        return head
