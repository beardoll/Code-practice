""" 题目
找出数组里最小的k个数
"""

class Solution:
    def heap_sort_for_top(self, heap):
        # heap has been established, but the top element is replaced
        # so we have to adjust the heap to keep the order
        val = heap[0]
        heap_idx = 0
        left_idx = 2*heap_idx + 1
        right_idx = 2*(heap_idx + 1)
        while left_idx < len(heap):
            if right_idx < len(heap):
                max_value = max([val, heap[left_idx], heap[right_idx]])
                if max_value == val:
                    break
                else:
                    heap[heap_idx] = max_value
                    heap_idx = right_idx
                    if max_value == heap[left_idx]:
                        heap_idx = left_idx
                    heap[heap_idx] = val
                    left_idx = 2*heap_idx + 1
                    right_idx = 2*(heap_idx + 1)
            else:
                if val > heap[left_idx]:
                    break
                else:
                    heap[heap_idx] = heap[left_idx]
                    heap[left_idx] = val
                    heap_idx = left_idx
                    left_idx = 2*heap_idx + 1
                    right_idx = 2*(heap_idx + 1)
        return heap 
    
    def heap_sort(self, tinput, k):
        # create maximum heap
        heap = []
        query_idx = 0
        for heap_idx in range(k):
            # down to top
            val = tinput[heap_idx]
            heap.append(val)
            heap_idx_child = heap_idx
            heap_idx_root = (heap_idx - 1) / 2.0
            while heap_idx_root >= 0:
                heap_idx_root = int(heap_idx_root)
                if heap[heap_idx_root] < val:
                    heap[heap_idx_child] = heap[heap_idx_root]
                    heap[heap_idx_root] = val
                heap_idx_child = heap_idx_root
                heap_idx_root = (heap_idx_root-1)/2.0
            
        if len(tinput) > k:
            for query_idx in range(k, len(tinput)):
                val = tinput[query_idx]
                if val < heap[0]:
                    heap[0] = val
                    heap = self.heap_sort_for_top(heap)
        
        # heap sort -> order list
        order_list = []
        order_list = [heap[0]]
        while len(heap) > 1:
            # exist when len(heap) == 1
            heap[0] = heap[-1]
            heap = heap[:-1]
            if len(heap) == 0: break
            heap = self.heap_sort_for_top(heap)
            order_list = [heap[0]] + order_list
            
        return order_list
    
    def fast_sort(self, unordered_list):
        # fast sort algorithm
        if len(unordered_list) <= 1:
            return unordered_list
        thresh = unordered_list[0]
        lt_list, gt_list = [], []
        for x in unordered_list[1:]:
            if x <= thresh:
                lt_list.append(x)
            else:
                gt_list.append(x)
        lt_list = self.fast_sort(lt_list)
        gt_list = self.fast_sort(gt_list)
        return lt_list + [thresh] + gt_list
        
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        #order_list = self.heap_sort(tinput, k)
        if len(tinput) == 0 or len(tinput) < k or k == 0:
            return []
        order_list = self.fast_sort(tinput)
        return order_list

if __name__ == '__main__':
    s = Solution()
    seq = [4, 5, 1, 6, 2, 7, 3, 8]
    heap = s.GetLeastNumbers_Solution(seq, 4)
    print(heap)
