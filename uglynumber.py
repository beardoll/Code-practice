class Solution:
    def GetUglyNumber_Solution(self, n):
        ugly_numbers = [1]
        while len(ugly_numbers) < n:
            largest_num = ugly_numbers[-1]
            cand_num = []
            for num in ugly_numbers:
                if 2*num > largest_num:
                    cand_num.append(num*2)
                elif 3*num > largest_num:
                    cand_num.append(num*3)
                elif 5*num > largest_num:
                    cand_num.append(num*5)
            new_inserted_num = min(cand_num)
            ugly_numbers.append(new_inserted_num)
        print(ugly_numbers)
        return ugly_numbers[-1]

if __name__ == '__main__':
    s = Solution()
    n = 8
    print(s.GetUglyNumber_Solution(n))
