""" 题目
请实现一个函数，用来判断一颗二叉树是不是对称的。
注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
"""

# coding=utf-8
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def InorderTraverse(self, pRoot):
        # non-recursive inorder traverse
        stack = []
        while pRoot is not None:
            stack.append(pRoot)
            pRoot = pRoot.left

        inorder_vals = []
        while len(stack) != 0:
            top_node = stack[-1]
            stack = stack[:-1]
            inorder_vals.append(top_node.val)
            top_node = top_node.right
            while top_node is not None:
                stack.append(top_node)
                top_node = top_node.left
                
        return inorder_vals
    
    def InorderReverseTraverse(self, pRoot):
        # non-recursive inorder traverse
        stack = []
        while pRoot is not None:
            stack.append(pRoot)
            pRoot = pRoot.right

        inorder_vals = []
        while len(stack) != 0:
            top_node = stack[-1]
            stack = stack[:-1]
            inorder_vals.append(top_node.val)
            top_node = top_node.left
            while top_node is not None:
                stack.append(top_node)
                top_node = top_node.right
                
        return inorder_vals

    def LastorderTraverse(self, pRoot):
        last_order_vals = []
        def left_first_search(stack):
            while stack[-1] is not None:
                node = stack[-1]
                if node.left is not None:
                    # 优先往左边走
                    if node.right is not None:
                        # 优先推入右节点
                        stack.append(node.right)
                    stack.append(node.left)
                else:
                    stack.append(node.right)
            # 推出最后一个None元素
            stack = stack[:-1]
            return stack

        # 初始化stack
        stack = [pRoot]
        while len(stack) > 0:
            stack = left_first_search(stack)
            top_node = stack[-1]
            stack = stack[:-1]
            last_order_vals.append(top_node.val)
            while True:
                if len(stack) == 0: break
                if stack[-1].left == top_node or stack[-1].right == top_node:
                    # 后继节点是其父节点
                    last_order_vals.append(stack[-1].val)
                    top_node = stack[-1]
                    stack = stack[:-1]
                else:
                    break
                
        return last_order_vals
    
    def isSymmetrical(self, pRoot):
        # write code here
        #inorder_vals = self.InorderTraverse(pRoot)
        #inorder_reverse_vals = self.InorderReverseTraverse(pRoot)
        #if inorder_vals == inorder_reverse_vals[::-1]:
        #    return True
        #else:
        #    return False
        lastorder_vals = self.LastorderTraverse(pRoot)
        print(lastorder_vals)

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
    s.isSymmetrical(node1)
