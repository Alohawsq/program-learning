"""
一个任务管理器系统可以让用户管理他们的任务，每个任务有一个优先级。这个系统需要高效地处理添加、修改、执行和删除任务的操作。
请你设计一个 TaskManager 类：
TaskManager(vector<vector<int>>& tasks) 初始化任务管理器，初始化的数组格式为 [userId, taskId, priority] ，
表示给 userId 添加一个优先级为 priority 的任务 taskId 。
void add(int userId, int taskId, int priority) 表示给用户 userId 添加一个优先级为 priority 的任务 taskId ，输入 保证 taskId 不在系统中。
void edit(int taskId, int newPriority) 更新已经存在的任务 taskId 的优先级为 newPriority 。输入 保证 taskId 存在于系统中。
void rmv(int taskId) 从系统中删除任务 taskId 。输入 保证 taskId 存在于系统中。
int execTop() 执行所有用户的任务中优先级 最高 的任务，如果有多个任务优先级相同且都为 最高 ，执行 taskId 最大的一个任务。执行完任务后，taskId 从系统中 删除 。
同时请你返回这个任务所属的用户 userId 。如果不存在任何任务，返回 -1 。
注意 ，一个用户可能被安排多个任务。
"""
import heapq
from typing import List

class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.heap = []
        self.task_dict = {}
        for task in tasks:
            userId, taskId, priority = task
            self.task_dict[taskId] = (userId, priority)
            heapq.heappush(self.heap, (-priority, -taskId, taskId))
    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.task_dict[taskId] = (userId, priority)
        heapq.heappush(self.heap, (-priority, -taskId, taskId))

    def edit(self, taskId: int, newPriority: int) -> None:
        userId, _ = self.task_dict[taskId]
        self.task_dict[taskId] = (userId, newPriority)
        heapq.heappush(self.heap, (-newPriority, -taskId, taskId))

    def rmv(self, taskId: int) -> None:
        if taskId in self.task_dict:
            del self.task_dict[taskId]

    def execTop(self) -> int:
        while self.heap:
            neg_pri, neg_tid, taskId = heapq.heappop(self.heap)
            if taskId not in self.task_dict:
                continue
            current_priority = self.task_dict[taskId][1]
            if current_priority != -neg_pri:
                continue
            userId = self.task_dict[taskId][0]
            del self.task_dict[taskId]
            return userId
        return -1

if __name__=='__main__':
    tasks = ["TaskManager", "add", "edit", "execTop", "rmv", "add", "execTop"]
    items = [[[[1, 101, 10], [2, 102, 20], [3, 103, 15]]], [4, 104, 5], [102, 8], [], [101], [5, 105, 15], []]
    tasks = ["TaskManager", "add", "edit", "execTop", "rmv", "add", "execTop"]
    items = [[[[1, 101, 8], [2, 102, 20], [3, 103, 5]]], [4, 104, 5], [102, 9], [], [101], [50, 101, 8], []]
    tasks = ["TaskManager", "rmv", "execTop"]
    items = [[[[10, 26, 25]]], [26], []]
    obj = None
    output = []
    for index, op in enumerate(tasks):
        if op == "TaskManager":
            obj = TaskManager(items[index][0])
            output.append(None)
        elif op == "add":
            obj.add(items[index][0], items[index][1], items[index][2])
            output.append(None)
        elif op == "edit":
            obj.edit(items[index][0], items[index][1])
            output.append(None)
        elif op == "execTop":
            result = obj.execTop()
            output.append(result) if result else output.append(None)
        elif op == "rmv":
            obj.rmv(items[index][0])
            output.append(None)
    print(f"***** output *****: {output}")

