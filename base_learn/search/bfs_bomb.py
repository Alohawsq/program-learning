"""
广度优先遍历寻找最佳炸弹放置位置
遍历矩阵记录矩阵中每个点的访问次数，访问次数最多的点
有问题需要再看
"""
from collections import deque

def bfs_bomb(matrix):
    # 记录行数和列数
    rows = len(matrix)
    cols = len(matrix[0]) if rows else 0
    # 添加标记矩阵
    visited = [[0 for _ in range(cols)] for _ in range(rows)]
    # 添加队列
    queue = deque()
    queue.append((0, 0))

    # 定义移动方向
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        x, y = queue.popleft()

        # 当前访问的值矩阵+1
        visited[x][y] += 1

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny]:
                queue.append((nx, ny))

    max_step = 0
    max_pos = (0, 0)
    for row, _rows in enumerate(visited):
        for col, step in enumerate(_rows):
            if (row, col) not in [(0, 0), (rows-1, cols-1)] and step >= max_step:
                max_pos = (row, col)
                max_step = step
    return max_pos

if __name__=='__main__':
    matrix = [[0] * 12 for _ in range(12)]
    pos = bfs_bomb(matrix)
    print(f"最多次被访问的坐标为：{pos}")
