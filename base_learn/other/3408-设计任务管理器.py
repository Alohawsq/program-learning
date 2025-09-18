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
        self.priority_to_taskId = {}
        self.taskId_info = {}
        for task in tasks:
            if task[2] not in self.priority_to_taskId:
                self.priority_to_taskId[task[2]] = [task[1]]
            else:
                self.priority_to_taskId[task[2]].append(task[1])
            # 记录task_id与userId和priority的关系
            self.taskId_info[task[1]] = [task[0], task[2]]
    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.taskId_info[taskId] = [userId, priority]
        if priority not in self.priority_to_taskId:
            self.priority_to_taskId[priority] = [taskId]
        else:
            self.priority_to_taskId[priority].append(taskId)

    def edit(self, taskId: int, newPriority: int) -> None:
        last_priority = self.taskId_info[taskId][1]
        self.taskId_info[taskId][1] = newPriority
        self.priority_to_taskId[last_priority].remove(taskId)
        if not self.priority_to_taskId[last_priority]:
            del self.priority_to_taskId[last_priority]
        if newPriority not in self.priority_to_taskId:
            self.priority_to_taskId[newPriority] = [taskId]
        else:
            self.priority_to_taskId[newPriority].append(taskId)

    def rmv(self, taskId: int) -> None:
        last_priority = self.taskId_info[taskId][1]
        del self.taskId_info[taskId]
        self.priority_to_taskId[last_priority].remove(taskId)
        if not self.priority_to_taskId[last_priority]:
            del self.priority_to_taskId[last_priority]

    def execTop(self) -> int:
        if not self.priority_to_taskId:
            return -1
        max_priority = max(list(self.priority_to_taskId.keys()))
        print(self.priority_to_taskId)
        max_task_id = max(self.priority_to_taskId[max_priority])
        userId = self.taskId_info[max_task_id][0]
        del self.taskId_info[max_task_id]
        self.priority_to_taskId[max_priority].remove(max_task_id)
        if not self.priority_to_taskId[max_priority]:
            del self.priority_to_taskId[max_priority]
        return userId


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

