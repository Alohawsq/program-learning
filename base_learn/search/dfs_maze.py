"""
深度优先遍历寻找最短路径
矩阵中指定起点坐标和终点坐标以及障碍物的位置最终返回最短步数
"""
def dfs_maze_short_path(matrix, start, end, obstacles):
    """
    使用DFS寻找矩阵中从起点到终点的最短路径步数

    参数:
    matrix: 二维矩阵，表示地图
    start: 元组 (x, y)，起点坐标
    end: 元组 (x, y)，终点坐标
    obstacles: 列表，包含障碍物坐标 [(x1, y1), (x2, y2), ...]

    返回:
    最短路径步数，如果无法到达则返回-1
    """
    # 获取矩阵的行数和列数
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0

    # 创建访问标记矩阵，初始化为False
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    # 标记障碍物位置为已访问（这样就不会走到障碍物上）
    for obs in obstacles:
        x, y = obs
        if 0 <= x < rows and 0 <= y < cols:
            visited[x][y] = True

    # 如果起点或终点是障碍物直接返回-1
    if visited[start[0]][start[1]] or visited[end[0]][end[1]]:
        return -1

    # 将最小步数设置为无穷大
    min_step = float('inf')

    # 定义四个移动方向：左、上、右、下
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def dfs(x, y, step):
        nonlocal min_step
        # 如果当前步数已经大于已知的最小步数，则提前终止
        if step >= min_step:
            return step

        # 如果到达终点则更新最小步数
        if (x, y) == end:
            min_step = min(min_step, step)
            return

        # 标记当前位置访问过
        visited[x][y] = True

        # 尝试四个方向
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # 如果新位置在矩阵中未被访问过则继续移动
            if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny]:
                dfs(nx, ny, step+1)
        # 回溯取消当前位置的标记
        visited[x][y] = False
    # 从起点开始DFS
    dfs(start[0], start[1], 0)
    # 如果没有找到路径，返回-1；否则返回最小步数
    return min_step if min_step != float('inf') else -1


if __name__=='__main__':
    matrix = [[0] * 5 for _ in range(5)]

    # 设置起点和终点
    start = (0, 0)
    end = (4, 4)

    # 设置障碍物
    obstacles = [(1, 1), (2, 2), (3, 3)]
    # 计算最短路径
    result = dfs_maze_short_path(matrix, start, end, obstacles)
    print(f"从起点{start}到终点{end}的最短路径步数是: {result}")
