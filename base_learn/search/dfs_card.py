"""
DFS遍历三盒三扑克牌方法排列
盒子1:牌1, 盒子2:牌2, 盒子3:牌3 → [1, 2, 3]
盒子1:牌1, 盒子2:牌3, 盒子3:牌2 → [1, 3, 2]
盒子1:牌2, 盒子2:牌1, 盒子3:牌3 → [2, 1, 3]
盒子1:牌2, 盒子2:牌3, 盒子3:牌1 → [2, 3, 1]
盒子1:牌3, 盒子2:牌1, 盒子3:牌2 → [3, 1, 2]
盒子1:牌3, 盒子2:牌2, 盒子3:牌1 → [3, 2, 1]
对一个盒子处理的主要的逻辑是：
    如果遍历到这个扑克没有被使用：
    1.将使用的几号扑克置为True
    2.将盒子数组的序号置为扑克号
然后递归处理下一个盒子
然后回溯
"""

def dfs_poke(boxes, poke):
    used = [False for _ in range(poke)]
    arr = [0 for _ in range(boxes)]
    result = []
    def dfs(depth):
        if depth == boxes:
            result.append(arr[:])  # 保存当前排列的副本
            return

        for index in range(poke):
            if not used[index]:
                used[index] = True
                arr[depth] = index + 1
                # 打印当前状态
                print(f"深度 {depth}: 将牌{index + 1}放入盒子{depth + 1}")
                # 递归处理下一个盒子
                dfs(depth+1)
                # 回溯
                used[index] = False
                arr[depth] = 0
    dfs(0)
    print(len(result))
    print(result)

def dfs_card(box_count, card_count):
    cards = [False for _ in range(card_count)]
    boxes = [0 for _ in range(box_count)]
    result = []

    def dfs(depth):
        if depth == box_count:
            result.append(boxes[:])
            return
        for index in range(card_count):
            if not cards[index]:
                cards[index] = True
                boxes[depth] = index + 1
                dfs(depth+1)
                cards[index] = False
                boxes[depth] = 0

    dfs(0)
    print(len(result))
    print(result)

if __name__=='__main__':
    # dfs_poke(3, 3)
    dfs_card(3, 3)