# -*- coding:utf-8 -*-
""" 题目
请实现一个函数用来匹配包括'.'和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（包含0次）。 
在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配

解题思路：递归求解
"""

class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
        if len(s) != 0 and len(pattern) == 0:
            # s不为空而pattern为空，肯定无法匹配
            return False
        if len(s) == 0 and len(pattern) == 0:
            # s和pattern同时为空，表示匹配上了
            return True
        if len(s) == 0 and len(pattern) != 0:
            # s为空，但是pattern不为空，需要进行判断
            # 首先，pattern的第二个字符必须为*，以消除第一个字符
            # 否则，肯定无法匹配
            if len(pattern) > 1 and pattern[1] == "*":
                return self.match(s, pattern[2:])
            else:
                return False

        # s和pattern都不为空的情况
        if s[0] == pattern[0]:
            if len(pattern) > 1 and pattern[1] == "*":
                # 如果s的第一个字符与pattern的第一个字符相同
                # 需要判断s字符重复出现的情况(如果pattern[1]为*号)：
                #    1. pattern[0]被消除，s匹配pattern[2:]
                #    2. pattern[0]被重复一次，s[1:]匹配pattern[2:]
                #    3. pattern[0]被重复两次以上，相当于变成了[pattern[0], pattern[0], *, ...], s[1:]匹配pattern
                return self.match(s, pattern[2:]) or self.match(s[1:], pattern[2:]) or self.match(s[1:], pattern)
            else:
                return self.match(s[1:], pattern[1:])
        else:
            # s[0] != pattern[0]
            if pattern[0] == ".":
                # 可替换
                if len(pattern) > 1 and pattern[1] == "*":
		    # .和*连在一起的情况
		    # .号可以被重复0， 1以及2次以上
                    return self.match(s, pattern[2:]) or self.match(s[1:], pattern[2:]) or self.match(s[1:], pattern)
                else:
                    return self.match(s[1:], pattern[1:])
            elif len(pattern) > 1 and pattern[1] == "*":
                # 消除pattern[0]
                return self.match(s, pattern[2:])
            else:
                return False

if __name__ == '__main__':
    s = "aaa"
    #pattern = "a.a"
    pattern = "ab*ac*a*"
    #pattern = "aa.a"
    #pattern = "ab*a"

    #s = "a"
    #pattern = "."

    sol = Solution()
    print(sol.match(s, pattern))
