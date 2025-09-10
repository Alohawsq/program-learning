"""
广度优先遍历寻找最佳炸弹放置位置
遍历矩阵记录矩阵中每个点的访问次数，访问次数最多的点
- '#' 表示不可炸的墙
- '%' 表示可炸的墙（假设）
- 'E' 表示敌人
- '.' 表示空地
"""
import collections


def bfs_count(grid, x, y):
    rows = len(grid)
    cols = len(grid[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    enemy_visited = set()
    queue = collections.deque()

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols:
            if grid[nx][ny] != '#':  # 不是不可炸墙则加入队列
                # 把移动的方向也传入到了队列中
                queue.append((nx, ny, (dx, dy)))

    while queue:
        i, j, d = queue.popleft()
        # 此后点的移动方向与上次点的移动方向相同
        if grid[i][j] == 'E' and (i, j) not in enemy_visited:
            enemy_visited.add((i, j))
        ni = i + d[0]
        nj = j + d[1]
        if 0 <= ni < rows and 0 <= nj < cols:
            if grid[ni][nj] != '#':
                queue.append((ni, nj, d))

    return len(enemy_visited)


if __name__ == "__main__":
    grid = [
        ['#', '%', 'E', '%', 'E'],
        ['#', '.', '.', 'E', '%'],
        ['%', '.', 'E', '%', '.'],
        ['%', 'E', '.', '%', 'E'],
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
                count = bfs_count(grid, i, j)  # 可以替换为 dfs_count(grid, i, j)
                if count > max_count:
                    max_count = count
                    best_pos = (i, j)

    if best_pos is None:
        print("No place to put the bomb.")
    else:
        print(f"The best position is {best_pos} with {max_count} enemies.")