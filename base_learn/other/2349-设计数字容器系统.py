"""
设计一个数字容器系统，可以实现以下功能：
在系统中给定下标处 插入 或者 替换 一个数字。
返回 系统中给定数字的最小下标。
请你实现一个 NumberContainers 类：
NumberContainers() 初始化数字容器系统
void change(int index, int number) 在下标 index 处填入 number 。如果该下标 index 处已经有数字了，那么用 number 替换该数字。
int find(int number) 返回给定数字 number 在系统中的最小下标。如果系统中没有 number ，那么返回 -1 。

"""

class NumberContainers:

    def __init__(self):
        ...
    def change(self, index: int, number: int) -> None:
        ...

    def find(self, number: int) -> int:
        ...



if __name__=='__main__':
    number = ["NumberContainers", "find", "change", "change", "change", "change", "find", "change", "find"]
    index = [[], [10], [2, 10], [1, 10], [3, 10], [5, 10], [10], [1, 20], [10]]
    obj = NumberContainers()
    obj.change(index, number)
    param_2 = obj.find(number)