"""
步骤：
读取网格，其中用0表示海洋，用1表示陆地（或者其它字符，具体根据问题）。
遍历每个单元格，如果是陆地且未被访问过，则从该点开始进行DFS或BFS，标记所有相连的陆地，并计算面积。
记录每次搜索到的岛屿面积，并更新最大面积。
"""

def num_islands_dfs(grid):
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

    def dfs(x, y):
        # 检查边界条件和是否已访问或是否是水域
        if x < 0 or x >= rows or y < 0 or y >= cols or grid[x][y] == '0' or visited[x][y]:
            return

        # 标记已访问
        visited[x][y] = True

        for dx, dy in directions:
            dfs(x + dx, y + dy)

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1' and not visited[i][j]:
                dfs(i, j)
                count += 1

    return count

def all_area_island_dfs(grid):
    # 计算行数和列数
    rows = len(grid)
    cols = len(grid[0]) if rows else 0
    # 设置标记数组
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    # 设置移动方向
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    areas = []
    def dfs(x, y):
        nonlocal area
        # 结束条件
        if x < 0 or x >= rows or y < 0 or y >= cols or grid[x][y] == '0' or visited[x][y]:
            return
        visited[x][y] = True
        area += 1

        for dx, dy in directions:
            nx, ny = dx + x, dy + y
            dfs(nx, ny)

    # 循环单元格
    for i in range(rows):
        for j in range(cols):
            area = 0
            if grid[i][j] == '1' and not visited[i][j]:
                dfs(i, j)
            areas.append(area) if area else None
    print(areas)
    return max(areas) if areas else 0

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

    print("\n使用DFS计算岛屿数量:", num_islands_dfs(grid))
    print("\n使用DFS计算所有岛屿面积:", all_area_island_dfs(grid))

