# -*- coding:utf-8 -*-
""" 题目
输入一颗二叉树的根节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
(注意: 在返回值的list中，数组长度大的数组靠前)
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def cmp(x, y):
    if len(y) < len(x):
        return 1
    if len(x) < (y):
        return -1
    return 0

class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def auxilary(self, root, expectNumber):
        # write code here
        if root is None:
            if expectNumber == 0: 
                return True, [[]]
            else:
                return False, [[]]
        if root.left is None and root.right is None:
            if root.val == expectNumber:
                return True, [[root.val]]
            else:
                return False, [[]]

        left_mark, lroute = self.auxilary(root.left, expectNumber - root.val)
        right_mark, rroute = self.auxilary(root.right, expectNumber - root.val)
        if not left_mark and not right_mark:
            return False, [[]]
        result = []
        if left_mark:
            for r in lroute:
                result.append([root.val] + r)

        if right_mark:
            for r in rroute:
                result.append([root.val] + r)
        
        sorted(result, cmp=cmp)
        return True, result

    def FindPath(self, root, expectNumber):
        mark, route = self.auxilary(root, expectNumber)
        if mark:
            return route
        else:
            return [[]]

if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(3)
    node3 = TreeNode(3)
    node1.left = node2
    node1.right = node3
    s = Solution()
    print(s.FindPath(node1, 4))
