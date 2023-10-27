class Queue:
    def __init__(self):
        self.data = []
        self.length = 0

    def queue(self, item):
        self.data.append(item)
        self.length += 1

    def dequeue(self):
        self.length -= 1
        return self.data.pop(0)

    def is_empty(self):
        return not self.data

    def get_first(self):
        return self.data[0]

    def __str__(self):
        return str(self.data)
