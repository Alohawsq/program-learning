"""
深度优先遍历寻找最佳炸弹放置位置
遍历矩阵记录矩阵中每个点的访问次数，访问次数最多的点
"""
def dfs_bomb(matrix):
    # 记录行数和列数
    rows = len(matrix)
    cols = len(matrix[0]) if rows else 0

    ...


if __name__=='__main__':
    matrix = [[0] * 5 for _ in range(5)]
    dfs_bomb(matrix)