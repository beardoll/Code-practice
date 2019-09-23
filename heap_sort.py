""" 堆排序练习
"""
import numpy as np

def create_heap(array):
    # 建堆算法，从heapSize / 2 - 1 -> 1开始逐渐调整堆
    # 建立最大堆
    # 算法复杂度为O(n)
    heap = array
    heap_size = len(heap)
    for i in range(int(heap_size / 2.0 - 1), -1, -1):
        root = i
        child_left = 2*i + 1
        child_right = 2*i + 2
        while child_left < heap_size:
            if child_right < heap_size:
                cur_val = heap[root] 
                left_val = heap[child_left]
                right_val = heap[child_right]
                if cur_val >= left_val and cur_val >= right_val:
                    # 调整完成
                    break
                else:
                    if left_val > right_val:
                        # 往左边调整
                        heap[child_left] = cur_val
                        heap[root] = left_val
                        root = child_left
                    else:
                        # 往右边调整
                        heap[child_right] = cur_val
                        heap[root] = right_val
                        root = child_right
            else:
                if cur_val >= left_val:
                    # 调整完成
                    break
                else:
                    # 往左边调整
                    heap[child_left] = cur_val
                    heap[root] = left_val
                    root = child_left
            
            child_left = 2*root + 1
            child_right = 2*root + 2
    return heap

def heap_sort(heap):
    # 给定一个最大堆，进行排序
    # 最大堆可以从小到大排
    # 最小堆可以从大到小排
    # 求topk问题，假如求topk最小，则建立最大堆
    def adjust_heap(heap):
        # 当heap root被更换后，调整heap使其恢复堆有序状态
        if len(heap) <= 1: return heap
        root = 0
        child_left = 1
        child_right = 2
        heap_size = len(heap)
        while child_left < heap_size:
            val = heap[root]
            val_left = heap[child_left]
            if child_right < heap_size:
                val_right = heap[child_right]
                if val >= val_left and val >= val_right:
                    # 已有序
                    break
                else:
                    if val_left > val_right:
                        # 最大值必为val_left
                        heap[child_left] = val
                        heap[root] = val_left
                        root = child_left
                    else:
                        # 最大值必为val_right
                        heap[child_right] = val
                        heap[root] = val_right
                        root = child_right
            else:
                if val >= val_left:
                    # 已有序
                    break
                else:
                    heap[child_left] = val
                    heap[root] = val_left
                    root = child_left
            child_left = 2*root + 1
            child_right = 2*root + 2
        return heap

    sorted_array = []
    heap_size = len(heap)
    for i in range(heap_size):
        sorted_array.append(heap[0])
        heap[0] = heap[-1]
        heap = heap[:-1]
        heap = adjust_heap(heap)

    return sorted_array

if __name__ == '__main__':
    array = [5, 6, 4, 3, 1, 7, 8]
    heap = create_heap(array)
    sorted_array = heap_sort(heap)
    print(sorted_array)
