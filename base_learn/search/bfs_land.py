"""
步骤：
读取网格，其中用0表示海洋，用1表示陆地（或者其它字符，具体根据问题）。
遍历每个单元格，如果是陆地且未被访问过，则从该点开始进行DFS或BFS，标记所有相连的陆地，并计算面积。
记录每次搜索到的岛屿面积，并更新最大面积。
"""
from collections import deque

def num_islands_bfs(grid):
    """
    计算岛屿数量
    """
    # 计算矩阵长宽
    rows = len(grid)
    cols = len(grid[0]) if rows else 0
    # 定义visited数组
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    # 定义移动方向
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    count = 0
    # 定义队列
    queue = deque()
    # 循环遍历每个单元格
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1' and not visited[i][j]:
                count += 1
                visited[i][j] = True
                queue.append((i, j))
                while queue:
                    x, y = queue.popleft()
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == '1' and not visited[nx][ny]:
                            visited[nx][ny] = True
                            queue.append((nx, ny))

    return count

def all_area_island_bfs(grid):
    ...



if __name__ == "__main__":
    # 示例网格
    grid = [
        ['1', '1', '0', '0', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '1', '0', '0'],
        ['0', '0', '0', '1', '1']
    ]

    print("网格:")
    for row in grid:
        print(row)
    print("使用BFS计算岛屿数量:", num_islands_bfs(grid))
    print("使用BFS计算所有岛屿面积:", all_area_island_bfs(grid))
