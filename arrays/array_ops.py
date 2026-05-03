class ArrayOps:
    def __init__(self):
        self.arr = []

    def insert(self, value):
        self.arr.append(value)

    def delete(self, value):
        if value in self.arr:
            self.arr.remove(value)

    def search(self, value):
        for i, v in enumerate(self.arr):
            if v == value:
                return i
        return -1

    def display(self):
        return self.arr


if __name__ == "__main__":
    arr = ArrayOps()
    arr.insert(10)
    arr.insert(20)
    print(arr.display())
