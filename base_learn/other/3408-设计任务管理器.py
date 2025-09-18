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
from typing import List

class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        ...
    def add(self, userId: int, taskId: int, priority: int) -> None:
        ...
    def edit(self, taskId: int, newPriority: int) -> None:
        ...

    def rmv(self, taskId: int) -> None:
        ...

    def execTop(self) -> int:
        ...

if __name__=='__main__':
    tasks = ["TaskManager","add","edit","execTop","rmv","add","execTop"]
    items = [[[[1, 101, 10], [2, 102, 20], [3, 103, 15]]], [4, 104, 5], [102, 8], [], [101], [5, 105, 15], []]
    obj = TaskManager(tasks)
    obj.add(userId,taskId,priority)
    obj.edit(taskId,newPriority)
    obj.rmv(taskId)
    param_4 = obj.execTop()