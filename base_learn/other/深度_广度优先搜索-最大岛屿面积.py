"""
计算🏝️最大面积
深度优先遍历
广度优先遍历
"""
from collections import deque

def get_max_area_dfs(grid):
    # 获取行和列值
    rows = len(grid)
    cols = len(grid[0]) if rows else 0
    # 定义标记数组
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    # 添加移动方向数组，上、下、左、右
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    # 标记最大面积
    max_area = 0
    # 定义深度优先遍历函数使用递归的方式调用
    def dfs(x, y):
        nonlocal area

        # 将该点在标记数组中设置为True
        visited[x][y] = True
        area += 1

        # 对该点进行移动探测
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny] and grid[nx][ny]:
                dfs(nx, ny)

    # 遍历数组从第一个不为0的点开始进行深度优先遍历
    for i in range(rows):
        for j in range(cols):
            area = 0
            if grid[i][j] and not visited[i][j]:
                dfs(i, j)
                if area > max_area:
                    max_area = area
    return max_area

def get_max_area_bfs(grid):
    # 计算行和列的值
    rows = len(grid)
    cols = len(grid[0]) if rows else 0
    # 定义标记数组
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    # 定义移动方向
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    max_area = 0

    queue = deque()
    # 遍历数组寻找不为0的点进行入队
    for i in range(rows):
        for j in range(cols):
            area = 0
            if grid[i][j] and not visited[i][j]:
                queue.append((i, j))
            while queue:
                x, y = queue.popleft()
                if not visited[x][y]:
                    visited[x][y] = True
                    area += 1
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] and not visited[nx][ny]:
                        queue.append((nx, ny))
            if area > max_area:
                max_area = area
    return max_area


if __name__=='__main__':
    grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    result = get_max_area_dfs(grid)
    print(f"获取到的最大岛屿面积为: {result}")
    result = get_max_area_bfs(grid)
    print(f"获取到的最大岛屿面积为: {result}")
