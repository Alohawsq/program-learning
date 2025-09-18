"""
设计一个数字容器系统，可以实现以下功能：
在系统中给定下标处 插入 或者 替换 一个数字。
返回 系统中给定数字的最小下标。
请你实现一个 NumberContainers 类：
NumberContainers() 初始化数字容器系统
void change(int index, int number) 在下标 index 处填入 number 。如果该下标 index 处已经有数字了，那么用 number 替换该数字。
int find(int number) 返回给定数字 number 在系统中的最小下标。如果系统中没有 number ，那么返回 -1 。

"""
import heapq

class NumberContainers:

    def __init__(self):
        self.index_to_num = {}
        self.num_to_heap = {}

    def change(self, index: int, number: int) -> None:
        if index in self.index_to_num and self.index_to_num[index] == number:
            return

        self.index_to_num[index] = number

        if number not in self.num_to_heap:
            self.num_to_heap[number] = []
        heapq.heappush(self.num_to_heap[number], index)

    def find(self, number: int) -> int:
        if number not in self.num_to_heap:
            return -1

        heap = self.num_to_heap[number]
        # 当堆顶元素与index_to_num中获取到的值不相等时，推出堆顶元素
        while heap and self.index_to_num.get(heap[0]) != number:
            heapq.heappop(heap)

        return heap[0] if heap else -1


if __name__=='__main__':
    number = ["NumberContainers", "find", "change", "change", "change", "change", "find", "change", "find"]
    index = [[], [10], [2, 10], [1, 10], [3, 10], [5, 10], [10], [1, 20], [10]]
    obj = NumberContainers()
    output = []
    for i, op in enumerate(number):
        if op == "find":
            result = obj.find(index[i][0])
            output.append(result) if result else output.append(None)
        elif op == "change":
            result = obj.change(index[i][0], index[i][1])
            output.append(result) if result else output.append(None)
        else:
            output.append(None)
    print(output)
