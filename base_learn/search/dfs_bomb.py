"""
深度优先遍历寻找最佳炸弹放置位置
遍历矩阵记录矩阵中每个点的访问次数，访问次数最多的点
"""
def dfs_count(grid, start_i, start_j):
    rows = len(grid)
    cols = len(grid[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    enemy_visited = set()
    stack = []

    for d in directions:
        ni = start_i + d[0]
        nj = start_j + d[1]
        if 0 <= ni < rows and 0 <= nj < cols:
            if grid[ni][nj] != '#':  # 不是不可炸墙则加入栈
                stack.append((ni, nj, d))

    while stack:
        i, j, d = stack.pop()
        if grid[i][j] == 'E' and (i, j) not in enemy_visited:
            enemy_visited.add((i, j))
        ni = i + d[0]
        nj = j + d[1]
        if 0 <= ni < rows and 0 <= nj < cols:
            if grid[ni][nj] != '#':
                stack.append((ni, nj, d))

    return len(enemy_visited)


if __name__ == "__main__":
    grid = [
        ['#', '%', 'E', '%', 'E'],
        ['#', '.', '.', 'E', '%'],
        ['%', '.', 'E', '%', '.'],
        ['%', '.', '.', '%', 'E'],
        ['%', '%', 'E', '%', 'E'],
    ]


    rows = len(grid)
    cols = len(grid[0])
    max_count = 0
    best_pos = None

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '.':
                # 使用BFS或DFS计算消灭敌人数
                count = dfs_count(grid, i, j)  # 可以替换为 dfs_count(grid, i, j)
                if count > max_count:
                    max_count = count
                    best_pos = (i, j)

    if best_pos is None:
        print("No place to put the bomb.")
    else:
        print(f"The best position is {best_pos} with {max_count} enemies.")