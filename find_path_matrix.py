""" 题目
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。
如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入该格子。 
例如:
    a b c e s f c s a d e e 
矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含"abcb"路径，
因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。
"""
import copy
class Solution:
    def search_next(self, matrix, mark, rows, cols, current_pos, path):
        # mark: 与matrix一样，是一个长度为rows * cols的数组，元素为False代表没走过
        # current_pos: (row, col)，当前所在位置
        # path: 剩余需要搜索的路径
        if len(path) == 0:
            return True

        c_row, c_col = current_pos
        next_steps = []
        if c_row > 0:
            # 可以向左走
            next_steps.append([c_row-1, c_col])

        if c_row < rows-1:
            # 可以向右走
            next_steps.append([c_row+1, c_col])

        if c_col > 0:
            # 可以向上走
            next_steps.append([c_row, c_col-1])

        if c_col < cols-1:
            # 可以向下走
            next_steps.append([c_row, c_col+1])

        succ = False
        for s in next_steps:
            pos = s[0] * cols + s[1]
            if not mark[pos] and matrix[pos] == path[0]:
                new_mark = copy.deepcopy(mark)
                new_mark[pos] = True
                if self.search_next(matrix, new_mark, rows, cols, s, path[1:]):
                    succ = True
                    break

        return succ

    def hasPath(self, matrix, rows, cols, path):
        # write code here
        mark = [False] * (rows * cols)
        succ = False
        for i in range(rows):
            for j in range(cols):
                pos = i*cols + j
                if matrix[pos] == path[0]:
                    new_mark = copy.deepcopy(mark)
                    new_mark[pos] = True
                    succ = succ or self.search_next(matrix, new_mark, rows, cols, [i, j], path[1:])

        return succ


if __name__ == '__main__':
    matrix = ['a', 'b', 'c', 'e', 's', 'f', 'c', 's', 'a', 'd', 'e', 'e']
    rows = 3
    cols = 4

    path = ['b', 'c', 'c', 'e', 'd']
    path = ['a', 'b', 'c', 'b']

    s = Solution()

    print(s.hasPath(matrix, rows, cols, path))

