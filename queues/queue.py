class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, val):
        self.queue.append(val)

    def dequeue(self):
        if self.is_empty():
            return "Queue Underflow"
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0


if __name__ == "__main__":
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    print(q.dequeue())
