""" 题目
给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。例如，
如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，那么一共存在6个滑动窗口，他们的最大值分别为{4,4,6,6,6,5}； 
针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个： 
{[2,3,4],2,6,2,5,1}， {2,[3,4,2],6,2,5,1}， {2,3,[4,2,6],2,5,1}， 
{2,3,4,[2,6,2],5,1}， {2,3,4,2,[6,2,5],1}， {2,3,4,2,6,[2,5,1]}。

思路:滑动窗口应当是队列，但为了得到滑动窗口的最大值，队列序可以从两端删除元素，因此使用双端队列。
原则：
 * 对新来的元素k，将其与双端队列中的元素相比较
 *   1）前面比k小的，直接移出队列（因为不再可能成为后面滑动窗口的最大值了!）,
 *   2）前面比k大的X，比较两者下标，判断X是否已不在窗口之内，不在了，直接移出队列
 *      队列的第一个元素是滑动窗口中的最大值
"""

class Solution:
    def maxInWindows(self, num, size):
        # write code here
        if size == 0 or size > len(num): return []
        biqueue = []
        anchor = 0
        for i in range(size):
            # 初始化biqueue
            if len(biqueue) == 0:
                biqueue.append([i, num[i]])
            else:
                del_pos = None
                for j, qv in enumerate(biqueue):
                    if biqueue[j][1] < num[i]:
                        del_pos = j

                if del_pos is not None:
                    biqueue[:del_pos+1] = []
                biqueue = [[i, num[i]]] + biqueue

        # 线性搜索，注意当前最大值的有效期
        max_nums_in_window = []
        for k in range(0, len(num) - size+1):
            if biqueue[-1][0] < k:
                biqueue = biqueue[:-1]
            # 窗口中的新值
            new_value = num[k+size-1]
            del_pos = None
            for j, qv in enumerate(biqueue):
                if biqueue[j][1] < new_value:
                    del_pos = j
            if del_pos is not None:
                biqueue[:del_pos+1] = []
            biqueue = [[k+size-1, new_value]] + biqueue
            max_nums_in_window.append(biqueue[-1][1])

        return max_nums_in_window

if __name__ == '__main__':
    array = [2, 3, 4, 2, 6, 2, 5, 1]
    size = 3

    s = Solution()
    print(s.maxInWindows(array, size))
