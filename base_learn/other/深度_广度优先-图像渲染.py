"""
有一幅以 m x n 的二维整数数组表示的图画 image ，其中 image[i][j] 表示该图画的像素值大小。
你也被给予三个整数 sr ,  sc 和 color 。你应该从像素 image[sr][sc] 开始对图像进行上色 填充 。
为了完成 上色工作：
从初始像素开始，将其颜色改为 color。
对初始坐标的 上下左右四个方向上 相邻且与初始像素的原始颜色同色的像素点执行相同操作。
通过检查与初始像素的原始颜色相同的相邻像素并修改其颜色来继续 重复 此过程。
当 没有 其它原始颜色的相邻像素时 停止 操作。
最后返回经过上色渲染 修改 后的图像 。
"""


def flood_fill(image, sr, sc, color):
    # 1.计算行和列的值
    rows = len(image)
    cols = len(image[0]) if rows else 0
    # 2.定义标记数组
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    # 3.定义递归函数
    def dfs(x, y, old_color):
        if image[x][y] == old_color and not visited[x][y]:
            image[x][y] = color
            visited[x][y] = True
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and image[nx][ny] == old_color and not visited[nx][ny]:
                    dfs(nx, ny, old_color)
    dfs(sr, sc, image[sr][sc])
    return image


if __name__=='__main__':
    image = [[1, 1, 1],
             [1, 1, 0],
             [1, 0, 1]]
    sr = 1
    sc = 1
    color = 2
    image = flood_fill(image, sr, sc, color)
    print(image)
