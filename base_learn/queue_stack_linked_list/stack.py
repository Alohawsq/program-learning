class Stack:
    def __init__(self):
        self.items = []

    def stack_push(self, item):
        self.items.append(item)
        return self.items

    def stack_pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def stack_top(self):
        if self.is_empty():
            return None
        return self.items[0]

    def stack_bottom(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def __str__(self):
        return str(self.items)
if __name__ == '__main__':
    stack = Stack()
    print("栈是否为空:", stack.is_empty())

    stack.stack_push(1)
    stack.stack_push(2)
    stack.stack_push(3)
    print("栈内容:", stack)
    print("栈大小:", stack.size())
    print("栈顶元素:", stack.stack_top())
    print("栈底元素:", stack.stack_bottom())

    print("出栈元素:", stack.stack_pop())
    print("出栈后栈:", stack)
    print("栈顶元素:", stack.stack_top())
    print("栈底元素:", stack.stack_bottom())

    print("出栈元素:", stack.stack_pop())
    print("出栈元素:", stack.stack_pop())
    print("出栈后栈:", stack)
    print("出栈元素(空栈时):", stack.stack_pop())
    print("栈是否为空:", stack.is_empty())