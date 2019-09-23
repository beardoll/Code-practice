""" 题目
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。

解法：建立一个辅助栈B
a) 当压入元素 <= top(B)时，将该元素压入；
b) 若从A中弹出的元素等于top(B)，则将top(B)弹出
c) 若B为空，则往A压入元素时，把该元素也压入B中
"""

class Solution:
    def __init__(self):
        self.stackA = []
        self.stackB = []

    def push(self, node):
        # write code here
        self.stackA = [node] + self.stackA
        if len(self.stackB) == 0:
            self.stackB.append(node)
        elif node <= self.stackB[0]:
            self.stackB = [node] + self.stackB

    def pop(self):
        # write code here
        node = self.stackA[0]
        del self.stackA[0]
        if node == self.stackB[0]:
            del self.stackB[0]
        return node

    def top(self):
        # write code here
        return self.stackA[0]

    def min(self):
        # write code here
        return self.stackB[0]

if __name__ == '__main__':
    order_list = ["PSH3","MIN","PSH4","MIN","PSH2","MIN","PSH3","MIN","POP","MIN","POP","MIN","POP","MIN","PSH0","MIN"]
    s = Solution()
    for order in order_list:
        if order.find("PSH") != -1:
            value = int(order[3:])
            s.push(value)
        elif order.find("MIN") != -1:
            print(s.min())
        else:
            v = s.pop()
