class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def peek(self):
        if self.is_empty():
            return None
        return self.items[0]

    def tail(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def __str__(self):
        return str(self.items)

if __name__ == '__main__':
    q = Queue()
    print("队列是否为空:", q.is_empty())

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print("队列内容:", q)
    print("队列大小:", q.size())
    print("队首元素:", q.peek())
    print("队尾元素:", q.tail())

    print("出队元素:", q.dequeue())
    print("出队后队列:", q)
    print("队首元素:", q.peek())
    print("队尾元素:", q.tail())

    print("出队元素:", q.dequeue())
    print("出队元素:", q.dequeue())
    print("出队后队列:", q)
    print("出队元素(空队列时):", q.dequeue())
    print("队列是否为空:", q.is_empty())





