""" 题目
有一个已排序的数组a，a中有正数也有负数，求a中绝对值不同的个数
"""

class Solution1:
    # NOTE: 这是我在面试时的做法，有点愚蠢
    def find_different_abs_num(self, sorted_array):
        # 设置负数指针neg_p，正数指针pos_p
        # 比较-array[neg_p]与array[pos_p]的大小
        # 若neg > pos，则计数加1，neg_p++，直到array[neg_p++]与当前array[neg_p]不同
        # 反之亦然。
        neg_p, pos_p = 0, len(sorted_array)-1
        neg_pass, pos_pass = False, False
        cnt = 0
        while neg_p != pos_p:
            if sorted_array[neg_p] > 0 or neg_p >= len(sorted_array):
                neg_pass = True
            if sorted_array[pos_p] < 0 or pos_p < 0:
                pos_pass = True
            if neg_pass and pos_pass:
                break
            if neg_pass:
                cnt += 1
                pos_p -= 1
                # eliminate repeated ones
                while pos_p >= 0 and sorted_array[pos_p] == sorted_array[pos_p+1]:
                    pos_p = pos_p - 1
                continue
            if pos_pass:
                cnt += 1
                neg_p += 1
                # eliminate repeated ones
                while neg_p < len(sorted_array) and sorted_array[neg_p] == sorted_array[neg_p-1]:
                    neg_p = neg_p + 1
                continue

            # neg_pass is False and pos_pass is False
            if -sorted_array[neg_p] == sorted_array[pos_p]:
                val = sorted_array[pos_p]
                cnt += 1
                neg_p += 1
                # eliminate repeated ones
                while neg_p < len(sorted_array) and -sorted_array[neg_p] == val:
                    neg_p += 1
                pos_p -= 1
                # eliminate repeated ones
                while pos_p >= 0 and sorted_array[pos_p] == val:
                    pos_p -= 1
            elif -sorted_array[neg_p] > sorted_array[pos_p]:
                val = sorted_array[neg_p]
                cnt += 1
                neg_p += 1
                # eliminate repeated ones
                while neg_p < len(sorted_array) and -sorted_array[neg_p] == val:
                    neg_p += 1
            else:
                val = sorted_array[pos_p]
                cnt += 1
                pos_p -= 1
                # eliminate repeated ones
                while pos_p > 0 and sorted_array[pos_p] == val:
                    pos_p -= 1
        return cnt

class Solution2:
    # 这是面试官给的标准做法
    def find_different_abs_num(self, sorted_array):
        # 实际上第一个数已经统计过了（可能是p1也可能是p2）
        # 因为prev_num进行了记录
        cnt = 1
        p1, p2 = 0, len(sorted_array)-1
        prev_num = max(abs(sorted_array[p1]), abs(sorted_array[p2]))
        while p1 != p2:
            if abs(sorted_array[p1]) == prev_num and p1 < p2:
                p1 += 1
            elif abs(sorted_array[p2]) == prev_num and p2 > p1:
                p2 -= 1
            else:
                if abs(sorted_array[p1]) > abs(sorted_array[p2]):
                    cnt += 1
                    prev_num = abs(sorted_array[p1])
                    p1 += 1
                elif abs(sorted_array[p1]) < abs(sorted_array[p2]):
                    cnt += 1
                    prev_num = abs(sorted_array[p2])
                    p2 -= 1
                else:
                    # equal
                    cnt += 1
                    prev_num = abs(sorted_array[p1])
                    p1 += 1
                    p2 -= 1
       
        if prev_num != abs(sorted_array[p1]):
            cnt += 1

        return cnt


if __name__ == '__main__':
    array1 = [-6, -4, -2, -1, -1, 0, 2, 3, 3, 4, 6]

    s = Solution2()
    print(s.find_different_abs_num(array1))
