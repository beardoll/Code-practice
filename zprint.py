""" 题目
请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，
第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。
"""
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def ZPrint(self, node_list, val_list, is_left_to_right):
        if len(node_list) == 0: return
        child_queue = []
        for node in node_list:
            if node is None: continue
            val_list.append(node.val)
            if is_left_to_right:
                # next will be right to left
                child_queue.append(node.left)
                child_queue.append(node.right)
            else:
                # next will be left to right
                child_queue.append(node.right)
                child_queue.append(node.left)
        self.ZPrint(child_queue[::-1], val_list, not is_left_to_right)
        
    def Print(self, pRoot):
        # write code here
        if pRoot == None: return []
        val_list = []
        self.ZPrint([pRoot], val_list, is_left_to_right=True)
        print(val_list)

if __name__ == '__main__':
    node1 = TreeNode(8)
    node2 = TreeNode(6)
    node3 = TreeNode(10)
    node4 = TreeNode(5)
    node5 = TreeNode(7)
    node6 = TreeNode(9)
    node7 = TreeNode(11)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7

    s = Solution()
    s.Print(node1)
