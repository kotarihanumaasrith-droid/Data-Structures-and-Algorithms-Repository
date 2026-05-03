class Stack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if self.is_empty():
            return "Stack Underflow"
        return self.stack.pop()

    def peek(self):
        return self.stack[-1] if not self.is_empty() else None

    def is_empty(self):
        return len(self.stack) == 0


if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    print(s.pop())
