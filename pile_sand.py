""" 题目
设有N堆沙子排成一排，其编号为1，2，3，…，N（N<=300）。每堆沙子有一定的数量，可以用一个整数来描述，
现在要将这N堆沙子合并成为一堆，每次只能合并相邻的两堆，合并的代价为这两堆沙子的数量之和，
合并后与这两堆沙子相邻的沙子将和新堆相邻，合并时由于选择的顺序不同，合并的总代价也不相同，

如有4堆沙子分别为:
    1  3  5  2 
我们可以
    a) 先合并1、2堆，代价为4，   -> 4 5 2 
    b) 又合并1，2堆，代价为9，   -> 9 2 
    c) 再合并得到11
    总代价为4+9+11=24
如果第二步是
    b') 先合并2，3堆，则代价为7  -> 4 7
    c') 最后一次合并代价为11
    总代价为4+7+11=22

问题是：找出一种合理的方法，使总的代价最小。输出最小代价。
"""

def get_min_one(array):
    min_v = None
    min_idx = 0
    for idx, x in enumerate(array):
        if min_v is None: min_v = x
        if x < min_v:
            min_v = x
            min_idx = idx

    return min_idx

def get_minimum_cost(sands):
    sands_before = sands
    weight_sums = []
    for i in range(len(sands) - 1):
        weight_sums.append(sands[i] + sands[i+1])

    cost = 0
    while len(weight_sums) > 0:
        # min_idx: 当前合并的沙子(在sands_before中是左边的那堆)
        min_idx = get_min_one(weight_sums)
        cur_cost = weight_sums[min_idx]
        cost += cur_cost
        if min_idx > 0:
            weight_sums[min_idx-1] += sands_before[min_idx+1]
        if min_idx < len(weight_sums)-1:
            weight_sums[min_idx+1] += sands_before[min_idx]
        del weight_sums[min_idx] 
        sands_before[min_idx+1] += sands_before[min_idx]
        del sands_before[min_idx]
        
    return cost

if __name__ == '__main__':
    sands = [1, 3, 5, 2]
    print(get_minimum_cost(sands))
