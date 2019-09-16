""" 题目
找出一个只包含"(“和”)"的字符串中最长的有效子字符串的长度。有效的意思是指该子字符串中的括号都能正确匹配。
e.g.:
    ) ( ) ( ( ) ) )
    0 1 2 3 4 5 6 7
以dp[i]表示以第i个字符为结尾的字符串最大长度，则
dp[0] = 0  dp[1] = 0  dp[2] = 2
dp[3] = 0  dp[4] = 0  dp[5] = 1
dp[6] = 6  dp[7] = 0
"""

def find_max_len(array):
    dp = [0]
    for idx, par in enumerate(array[1:]):
        # start from the second parenthese
        if par == '(':
            dp.append(0)
            continue

        idx_bak = idx
        l = 0
        
        #while dp[idx_bak] != 0 and idx_bak >= 0:
        l += dp[idx_bak]
        idx_bak -= dp[idx_bak]

        if array[idx_bak] == ")":
            dp.append(0)
            continue

        l += 2
        idx_bak -= 1

        #while dp[idx_bak] != 0 and idx_bak >= 0:
        l += dp[idx_bak]
        idx_bak -= dp[idx_bak]
            
        dp.append(l)

    return dp

if __name__ == '__main__':
    array = [')', '(', ')', '(', '(', ')', ')', ')']
    print(find_max_len(array))

        

