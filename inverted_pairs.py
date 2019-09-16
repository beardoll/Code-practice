""" 题目
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
输入一个数组,求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。 即输出P%1000000007
"""

class Solution0:
    def quick_search(self, ordered_list, value):
        # 利用快排寻找value元素的位置
        # 此方法超时
        if len(ordered_list) == 0:
            return 0
        
        if len(ordered_list) == 1:
            if ordered_list[0] > value:
                return 0
            else:
                return -1
            
        mid = int(len(ordered_list)/2.0)
        pos = 0
        if value >= ordered_list[mid]:
            pos = self.quick_search(ordered_list[:mid], value)
        else:
            pos = self.quick_search(ordered_list[mid:], value) + mid
        return pos
    
    def InversePairs(self, data):
        # write code here
        ordered_list = [data[0]]
        ipairs = 0
        for x in data[1:]:
            pos = self.quick_search(ordered_list, x)
            print(pos)
            ordered_list = ordered_list[:pos+1] + [x] + ordered_list[pos+1:]
            ipairs += pos + 1
        return ipairs % 1000000007

class Solution1:
    def MergeSort(self, data):
        # 利用mergesort，求得逆序对的数目
        # 逆序对的数目等于数字移动steps数的一半（即向后移动步数/向前移动步数）
        # ascend sort
        if len(data) <= 1:
            return data, 0
        mid = int(len(data)/2)
        data_left = data[:mid]
        data_right = data[mid:]
        data_left_sort, cnt1 = self.MergeSort(data_left)
        data_right_sort, cnt2  = self.MergeSort(data_right)
        move_steps = cnt1 + cnt2
        i, j = 0, 0
        move_steps_merge = 0
        data_sort = []
        while i < len(data_left_sort) and j < len(data_right_sort):
            if data_left_sort[i] < data_right_sort[j]:
                data_sort.append(data_left_sort[i])
                i += 1
            else:
                data_sort.append(data_right_sort[j])
                move_steps_merge += j + len(data_left_sort) - (i+j)
                j += 1
        if i < len(data_left_sort):
            data_sort += data_left_sort[i:]
        
        if j < len(data_right_sort):
            data_sort += data_right_sort[j:]

        return data_sort, move_steps + move_steps_merge

    def InversePairs(self, data):
        data_sort, move_steps = self.MergeSort(data)
        print(data_sort)
        return move_steps

if __name__ == '__main__':
    a_list = [1,2,3,4,5,6,7,0]
    s = Solution1()
    print(s.InversePairs(a_list))
