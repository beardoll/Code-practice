""" 题目
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
"""

import functools

def cmp(x, y):
    if y < x:
        return 1
    if x < y:
        return -1
    return 0

def cmp_str(x, y):
    str1 = x + y
    str2 = y + x
    if int(str1) > int(str2):
        return 1
    elif int(str1) < int(str2):
        return -1
    else:
        return 0

# numbers = [5, 2, 9, 7]
# print(sorted(numbers, key=functools.cmp_to_key(cmp)))

array = ['3', '32', '321']
print(sorted(array, key=functools.cmp_to_key(cmp_str)))


