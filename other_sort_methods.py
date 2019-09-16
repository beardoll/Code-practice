"""
排序算法测试
"""

def fast_sort(unordered_list):
    if len(unordered_list) <= 1:
        return unordered_list
    thresh = unordered_list[0]
    lt_list, gt_list = [], []
    for x in unordered_list[1:]:
        if x <= thresh:
            lt_list.append(x)
        else:
            gt_list.append(x)
    lt_list = fast_sort(lt_list)
    gt_list = fast_sort(gt_list)
    return lt_list + [thresh] + gt_list

def merge_sort(unordered_list):
    if len(unordered_list) <= 1:
        return unordered_list
    mid = int(len(unordered_list) / 2)
    left_part = unordered_list[:mid]
    right_part = unordered_list[mid:]
    # sort each part
    left_part = merge_sort(left_part)
    right_part = merge_sort(right_part)
    sorted_list = []
    i, k = 0, 0
    while i < len(left_part) and k < len(right_part):
        if left_part[i] < right_part[k]:
            sorted_list.append(left_part[i])
            i += 1
        else:
            sorted_list.append(right_part[k])
            k += 1
    if i < len(left_part):
        sorted_list += left_part[i:]
    if k < len(right_part):
        sorted_list += right_part[k:]
    
    return sorted_list

if __name__ == '__main__':
    unordered_list = [5, 3, 2, 5, 6, 4, 8, 7, 4]
    #ordered_list = fast_sort(unordered_list)
    ordered_list = merge_sort(unordered_list)
    print(ordered_list)
