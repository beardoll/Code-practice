""" 构造线段树，实现任意区间和的查询，以及任意元素的修改
简单起见，假设数组是偶数个数
"""
class TreeNode:
    def __init__(self, interval, value):
        self.interval = interval
        self.value = value
        self.left = None
        self.right = None

class TreeStructure:
    # 这种结构很难做修改。。。
    def __init__(self, array):
        self.root_node = self.create_index_tree(array)

    def create_index_tree(self, array):
        # 构造线段树（自下而上?）
        # 返回树的根节点
        # 为每个元素建立一个节点
        last_nodes = []
        for idx, item in enumerate(array):
            tree_node = TreeNode([idx, idx+1], item)
            last_nodes.append(tree_node)
        
        while len(last_nodes) > 1:
            new_last_nodes = []
            for idx in range(0, len(last_nodes), 2):
                left_child_node = last_nodes[idx]
                right_child_node = last_nodes[idx+1]
                new_interval = [left_child_node.interval[0], right_child_node.interval[1]]
                new_value = left_child_node.value + right_child_node.value
                new_node = TreeNode(new_interval, new_value)
                new_node.left = left_child_node
                new_node.right = right_child_node
                new_last_nodes.append(new_node)
            if len(last_nodes) % 2 != 0:
                new_last_nodes.append(last_nodes[-1])
            last_nodes = new_last_nodes

        return last_nodes[0]

    def do_query(self, query_interval):
        return self.query(self.root_node, query_interval)

    def query(self, tree_node, query_interval):
        # 查询区间和
        # 算法复杂度应为O(logn)??
        # tree_node指代树/子树的根节点
        if tree_node.left is None and tree_node.right is None:
            return tree_node.value

        if tree_node.right is None:
            # 左孩子不为空，右孩子为空
            return self.query(tree_node.left, query_interval)

        # 左右孩子都不为空
        cur_interval = tree_node.interval
        left_child = tree_node.left
        right_child = tree_node.right
        left_interval = left_child.interval
        right_interval = right_child.interval
        if query_interval[0] >= right_interval[0]:
            # 只需要在右子树搜索
            return self.query(right_child, query_interval)
        elif query_interval[1] <= left_interval[1]:
            # 只需要在左子树搜索
            return self.query(left_child, query_interval)
        else:
            query_interval_left = [query_interval[0], left_interval[1]]
            query_interval_right = [right_interval[0], query_interval[1]]
            return self.query(left_child, query_interval_left) + self.query(right_child, query_interval_right)

class ArrayStructure:
    # 数组形式的线段树
    def __init__(self, array):
        self.array = array
        self.index_array = self.build(array)
        self.tree_size = len(self.index_array)

    def build(self, array):
        last_elements = []
        for idx, item in enumerate(array):
            last_elements.append({'interval': [idx, idx+1], 'value': item})
        index_array = last_elements
        while len(last_elements) > 1:
            new_last_elements = []
            for idx in range(0, len(last_elements), 2):
                left_element = last_elements[idx]
                right_element = last_elements[idx+1]
                interval_left, value_left = left_element['interval'], left_element['value']
                interval_right, value_right = right_element['interval'], right_element['value']
                new_element = {'interval': [interval_left[0], interval_right[1]], 'value': value_left + value_right}
                new_last_elements.append(new_element)
            index_array = new_last_elements + index_array
            if len(last_elements) % 2 != 0:
                odd_element = last_elements[-1]
                last_elements = new_last_elements + [odd_element]
            else:
                last_elements = new_last_elements
        return index_array

    def query(self, tree_idx, query_interval):
        # tree_idx: 指代当前搜索的树/子树的根节点
        left_tree_idx = 2*tree_idx+1
        right_tree_idx = 2*tree_idx+2
        if left_tree_idx >= self.tree_size:
            # 叶子节点
            return self.index_array[tree_idx]['value']

        if right_tree_idx >= self.tree_size:
            # 仅有左子树
            return self.query(2*tree_idx+1, query_interval)

        # 左右子树都存在
        left_tree_node = self.index_array[left_tree_idx]
        right_tree_node = self.index_array[right_tree_idx]
        left_interval, left_value = left_tree_node['interval'], left_tree_node['value']
        right_interval, right_value = right_tree_node['interval'], right_tree_node['value']
        if query_interval[1] <= left_interval[1]:
            return self.query(left_tree_idx, query_interval)
        elif query_interval[0] >= right_interval[0]:
            return self.query(right_tree_idx, query_interval)
        else:
            return self.query(left_tree_idx, [query_interval[0], left_interval[1]]) + \
                    self.query(right_tree_idx, [right_interval[0], query_interval[1]])

    def update(self, idx_in_array, new_value):
        # 将array中idx_in_array的位置替换为new_value
        idx_in_index_array = len(self.index_array) - (len(self.array) - idx_in_array)
        self.index_array[idx_in_index_array]['value'] = new_value
        while idx_in_index_array > 0:
            if idx_in_index_array % 2 == 1:
                brother_idx = int(idx_in_index_array + 1)
                father_idx = int((idx_in_index_array - 1) / 2)
            else:
                brother_idx = int(idx_in_index_array - 1)
                father_idx = int(idx_in_index_array / 2 - 1)
            self.index_array[father_idx]['value'] = self.index_array[idx_in_index_array]['value'] +\
                    self.index_array[brother_idx]['value']
            idx_in_index_array = father_idx

    def do_query(self, query_interval):
        return self.query(0, query_interval)

if __name__ == '__main__':
    array = [1, 2, 3, 4, 5, 6, 7, 8]
    query_interval = [0, 5]
    
    # t = TreeStructure(array)
    # print(t.do_query(query_interval))

    a = ArrayStructure(array)
    a.update(4, 10)
    print(a.do_query(query_interval))

