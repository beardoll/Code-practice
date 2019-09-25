# -*- coding:utf-8 -*-
""" 题目
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
"""

class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if len(numbers) == 1: return 1
        cand = numbers[0] 
        cnt = 1
        for num in numbers[1:]:
            if cnt == 0:
                cand = num
                cnt = 1
                continue

            if cand == num:
                cnt += 1
            else:
                cnt -= 1
        
        l = len(numbers)
        cnt_cand = 0
        for num in numbers:
            # 再搜索一遍，判断cand是不是众数
            if cand == num:
                cnt_cand += 1

        if cnt_cand > l / 2.0:
            return cand
        else:
            return 0

if __name__ == '__main__':
    numbers = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    #numbers = [1, 0, 1]
    s = Solution()
    print(s.MoreThanHalfNum_Solution(numbers))
