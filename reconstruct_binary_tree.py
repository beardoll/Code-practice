class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre) == 0:
            return None
        elif len(pre) == 1:
            return TreeNode(pre[0])
        else:
            head_ele = pre[0]
            head_node = TreeNode(head_ele)
            left_ele_pre = []
            right_ele_pre = []
            left_ele_tin = []
            right_ele_tin = []
            reading_to_left = True
            for idx in range(1, len(pre)):
                if tin[idx-1] == head_ele:
                    reading_to_left = False
                if reading_to_left:
                    left_ele_pre.append(pre[idx])
                    left_ele_tin.append(tin[idx-1])
                else:
                    right_ele_pre.append(pre[idx])
                    right_ele_tin.append(tin[idx])
            head_node.left = self.reConstructBinaryTree(left_ele_pre, left_ele_tin)
            head_node.right = self.reConstructBinaryTree(right_ele_pre, right_ele_tin)
            return head_node

if __name__ == '__main__':
    pre = [1,2,3,4,5,6,7]
    tin = [3,2,4,1,6,5,7]
    s = Solution()
    head_node = s.reConstructBinaryTree(pre, tin)
    print("Header of the tree is {}, left is {}, right is {}".format(head_node.val, head_node.left.val, head_node.right.val))
    
