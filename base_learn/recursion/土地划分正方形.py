"""
分而治之
输入土地长宽，对土地进行划分，要求均匀的划分为大小相同的正方形
基线条件：当长是宽的整数倍
缩小问题规模：如果长不是宽的整数倍，则找出其中最大的正方形，对小的长方形继续划分
"""

def solution(n, m):
    # 较长的一边定义为长，较短的一边定义为宽
    length = max(n, m)
    width = min(n, m)
    # 定义基线条件
    if not length % width:
        return width
    # 缩小问题规模
    return solution(length % width, width)


if __name__=='__main__':
    result = solution(640, 400)
    print(f"均匀分割的正方形的边长为: {result}")