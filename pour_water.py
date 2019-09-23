""" 题目
有一个装满了8L水的满壶，一个5L容量的空壶，一个3L容量的空壶
现在想通过倒满/倒空的操作，使得正好有一个壶装了4L的水

思路：
前向算法 + 队列，更新的状态放在队尾，直到搜索到目标状态
"""

# state: 8, 5, 3L壶的容量
# action: 倒水操作

def get_best_route():
    queue = [{'state': [8, 0, 0], 'route': []}]
    best_route = None

    while True:
        item = queue[0]
        del queue[0]
        a, b, c = item['state']
        route = item['route']
        # a -> b
        if a > 0 and b < 5:
            # 可倒水
            state_transfer = [a - (min(a+b, 5)-b), min(a+b, 5), c]
            new_route = route + ['ab']
            if (state_transfer[0] == 4 or state_transfer[1] == 4) and state_transfer[2] > 0:
                best_route = new_route
                break
            new_item = {'state': state_transfer, 'route': new_route}
            queue.append(new_item)

        # a -> c
        if a > 0 and c < 3:
            state_transer = [a - (min(a+c, 3)-c), b, min(a+c, 3)]
            new_route = route + ['ac']
            if (state_transfer[0] == 4 or state_transfer[1] == 4) and state_transfer[2] > 0:
                best_route = new_route
                break
            new_item = {'state': state_transfer, 'route': new_route}
            queue.append(new_item)
        
        # b -> a
        # a壶容量永远足够接受其他壶的水
        if b > 0:
            state_transfer = [a+b, 0, c]
            new_route = route + ['ba']
            if (state_transfer[0] == 4 or state_transfer[1] == 4) and state_transfer[2] > 0:
                best_route = new_route
                break
            new_item = {'state': state_transfer, 'route': new_route}
            queue.append(new_item)

        # b -> c
        if b > 0 and c < 3:
            state_transfer = [a, b - (min(b+c, 3) - c), min(b+c, 3)]
            new_route = route + ['bc']
            if (state_transfer[0] == 4 or state_transfer[1] == 4) and state_transfer[2] > 0:
                best_route = new_route
                break
            new_item = {'state': state_transfer, 'route': new_route}
            queue.append(new_item)

        # c -> a
        if c > 0:
            state_transfer = [a+c, b, 0]
            new_route = route + ['ca']
            if (state_transfer[0] == 4 or state_transfer[1] == 4) and state_transfer[2] > 0:
                best_route = new_route
                break
            new_item = {'state': state_transfer, 'route': new_route}
            queue.append(new_item)

        # c -> b
        if b < 5 and c > 0:
            state_transfer = [a, min(b+c, 5), c - (min(b+c, 5) - b)]
            new_route = route + ['cb']
            if (state_transfer[0] == 4 or state_transfer[1] == 4) and state_transfer[2] > 0:
                best_route = new_route
                break
            new_item = {'state': state_transfer, 'route': new_route}
            queue.append(new_item)

if __name__ == '__main__':
    best_route = get_best_route()
    print(best_route)
