"""
给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。
单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
"""
from  collections import deque

# 不要在遇到第一个方向时就会返回，不管这个方向是否成功，应该对结果判断如果移动后此方向不对继续进行其他方向的搜索
def search_word_dfs(board, word):
    # 1.计算行列大小
    rows = len(board)
    cols = len(board[0]) if rows else 0
    # 2.定义标记数组
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    # 3.定义移动方向
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    # 4.定义递归函数
    def dfs(x, y, i):
        if i == len(word) - 1:
            return True
        visited[x][y] = True
        i += 1

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny] and board[nx][ny] == word[i]:
                if dfs(nx, ny, i):
                    return True
                visited[nx][ny] = False
        visited[x][y] = False

    for i in range(rows):
        for j in range(cols):
            if board[i][j] == word[0]:
                result = dfs(i, j, 0)
                if result:
                    return True
    return False

# BFS不适用于需要跟踪完整路径的问题,BFS通常用于最短路径等问题，而单词搜索问题需要记录路径（即已访问的节点），
# 因此直接使用BFS会面临状态爆炸的问题，因为每个路径的已访问节点集合不同。
def search_word_bfs(board, word):
    if not board or not word:
        return False

    rows = len(board)
    cols = len(board[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # 遍历网格中的每个单元格，寻找起始点
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == word[0]:
                # 对于每个起始点，使用BFS
                # 队列元素：(x, y, index, visited_set)
                # visited_set使用frozenset来存储已访问的坐标
                queue = deque()
                initial_visited = frozenset([(i, j)])
                queue.append((i, j, 0, initial_visited))

                while queue:
                    x, y, index, visited = queue.popleft()

                    # 如果已经匹配到单词的最后一个字符，返回成功
                    if index == len(word) - 1:
                        return True

                    # 尝试四个方向
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy

                        # 检查新位置是否有效且未被访问，且字符匹配
                        if (0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited and board[nx][ny] == word[index + 1]):
                            # 创建新的访问集合，包含当前路径的所有已访问点
                            new_visited = set(visited)
                            new_visited.add((nx, ny))
                            new_visited = frozenset(new_visited)

                            queue.append((nx, ny, index + 1, new_visited))

    return False

if __name__=='__main__':
    # board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']]
    # board = [["a","b"],["c","d"]]
    # board = [["C", "A", "A"],
    #          ["A", "A", "A"],
    #          ["B", "C", "D"]]
    # board = [["A","B","C","E"],
    #          ["S","F","C","S"],
    #          ["A","D","E","E"]]
    board = [["A","B","C","E"],
             ["S","F","E","S"],
             ["A","D","E","E"]]
    # word = "ABCCED"
    # word = "cdba"
    # word = "AAB"
    # word = "ABCB"
    word = "ABCESEEEFS"
    result= search_word_dfs(board, word)
    print(f"搜索单词的结果为: {result}")
    result = search_word_bfs(board, word)
    print(f"搜索单词的结果为: {result}")