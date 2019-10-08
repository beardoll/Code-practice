# -*- coding:utf-8 -*-
""" 题目
输入一个链表，输出该链表中倒数第k个结点。
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution1:
    def FindKthToTail(self, head, k):
        # write code here
        prev_node = ListNode(head.val)
        head = head.next
        while head is not None:
            cur_node = ListNode(head.val)
            cur_node.next = prev_node
            prev_node = cur_node
            head = head.next

        # prev_node is point to the tail of the original linklist
        for _ in range(k-1):
            prev_node = prev_node.next
            if prev_node is None:
                # k is larger than the length of the linklist
                return None

        return prev_node.val

class Solution2:
    def FindKthToTail(self, head, k):
        # write code here
        head1 = head
        head2 = head
        while k > 1:
            # 让head1先走k-1步
            head1 = head1.next
            if head1 is None:
                return None
            else:
                k = k - 1
                continue

        # head1与head2齐头并进
        while head1.next is not None:
            head1 = head1.next
            head2 = head2.next

        return head2.val
        
def construct_linklist(array):
    head = ListNode(array[0])
    prev_node = head
    for x in array[1:]:
        cur_node = ListNode(x)
        prev_node.next = cur_node
        prev_node = cur_node

    return head

if __name__ == '__main__':
    array = [1, 2, 3, 4, 5]
    head = construct_linklist(array)
    k = 1

    s = Solution2()
    print(s.FindKthToTail(head, k))


