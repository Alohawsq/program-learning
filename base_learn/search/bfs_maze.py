"""
广度优先遍历寻找最短路径
矩阵中指定起点坐标和终点坐标以及障碍物的位置最终返回最短步数
"""
from collections import deque

def bfs_maze_short_path(matrix, start, end, obstacles):
    """
        使用BFS寻找矩阵中从起点到终点的最短路径步数

        参数:
        matrix: 二维矩阵，表示地图
        start: 元组 (x, y)，起点坐标
        end: 元组 (x, y)，终点坐标
        obstacles: 列表，包含障碍物坐标 [(x1, y1), (x2, y2), ...]

        返回:
        最短路径步数，如果无法到达则返回-1
        """
    # 获取行数和列数
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0

    # 定义visited矩阵
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    # 障碍物位置标记为已访问
    for obs in obstacles:
        if 0 <= obs[0] < rows and 0 <= obs[1] <= cols:
            visited[obs[0]][obs[1]] = True

    # 如果开始和结束位置是障碍物则返回-1
    if visited[start[0]][start[1]] or visited[end[0]][end[1]]:
        return -1

    # 定义四个移动方向：左、上、右、下
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    # 创建队列
    queue = deque()
    queue.append((start[0], start[1], 0))

    while queue:
        x, y, step = queue.popleft()
        # 设置当前节点已访问
        visited[x][y] = True

        # 如果到达终点则结束
        if (x, y) == end:
            return step

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny]:
                queue.append((nx, ny, step+1))


    return step

if __name__=='__main__':
    matrix = [[0] * 5 for _ in range(5)]

    # 设置起点和终点
    start = (0, 0)
    end = (4, 4)

    # 设置障碍物
    obstacles = [(1, 1), (2, 2), (3, 3)]
    # 计算最短路径
    result = bfs_maze_short_path(matrix, start, end, obstacles)
    print(f"从起点{start}到终点{end}的最短路径步数是: {result}")