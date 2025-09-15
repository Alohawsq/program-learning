"""
有两个水壶，容量分别为 x 和 y 升。水的供应是无限的。确定是否有可能使用这两个壶准确得到 target 升。
允许的操作
装满任意一个水壶
清空任意一个水壶
将水从一个水壶倒入另一个水壶，直到接水壶已满，或倒水壶已空。
"""

def can_measure_water(x, y, target):
    visited = set()
    # 初始水量为0,0
    stack = [(0, 0)]
    while stack:
        # a表示第一个水壶的水量，b表示第二个水壶的水量
        a, b = stack.pop()
        # 如果a的水量等于target或者b的水量等于target或者a+b等于target
        if a == target or b == target or a + b == target:
            return True
        # 如果已经访问过这个状态，跳过
        if (a, b) in visited:
            continue
        # 将这个状态加入已访问集合
        visited.add((a, b))
        # 生成所有可能的下一个状态
        next_states = []
        # 装满第一个水壶
        next_states.append((x, b))
        # 装满第二个水壶
        next_states.append((a, y))
        # 倒空第一个水壶
        next_states.append((0, b))
        # 倒空第二个水壶
        next_states.append((a, 0))
        # 从第一个水壶倒入第二个水壶
        next_states.append((max(0, a - (y - b)), b + min(a, y - b)))
        # 从第二个水壶倒入第一个水壶
        next_states.append((a + min(b, x - a), max(0, b - (x - a))))
        for next_state in next_states:
            # 如果下一个状态是目标状态，返回步数
            if next_state not in visited:
                stack.append(next_state)
    return False


if __name__=='__main__':
    x = 3
    y = 5
    target = 4
    print(can_measure_water(x, y, target))

