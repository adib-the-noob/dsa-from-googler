class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

stack1 = Stack()
stack1.push(1)
stack1.push(2)
stack1.push(3)
print(stack1.items)
