""" 题目
输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，
另一个特殊指针指向任意一个节点），返回结果为复制后复杂链表的head。
（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
"""

# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        pPre = pHead
        pNext = pHead.next
        while pPre is not None:
            pCopy = RandomListNode(pPre.label)
            pCopy.next = pNext
            pPre.next = pCopy
            pPre = pNext
            if pNext is not None:
                pNext = pNext.next
       
        p = pHead
        while p is not None:
            if p.random is not None:
                p.next.random = p.random.next
            p = p.next.next
        
        # detach
        pCopyHead = pHead.next
        p = pCopyHead
        while p.next is not None:
            tmp = p.next.next
            p.next = p.next.next
            p = tmp

        return pCopyHead

if __name__ == '__main__':
    node1 = RandomListNode(1)
    node2 = RandomListNode(2)
    node3 = RandomListNode(3)
    node4 = RandomListNode(4)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node1.random = node3
    node3.random = node4

    s = Solution()
    pHead = s.Clone(node1)
    while pHead is not None:
        print(pHead.label)
        pHead = pHead.next
