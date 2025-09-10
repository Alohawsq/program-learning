class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f"{self.data}"

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """
        在链表末尾添加节点
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def prepend(self, data):
        """
        在链表开头添加节点
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, prev_node, data):
        """
        在指定节点后插入新节点
        """
        if not prev_node:
            print("Previous node is not in the list")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):
        """
        删除节点
        """
        ...

    def search_node(self, key):
        """
        查找节点是否存在
        """
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    def length(self):
        """
        获取链表长度
        """
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def print_list(self):
        """
        打印链表
        """
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")
