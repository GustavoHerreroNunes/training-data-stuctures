class Stack:
    def __init__(self):
        self.data = []
        self.length = 0

    def stack_up(self, item):
        self.length += 1
        self.data.insert(0, item)

    def unstack(self):
        self.length -= 1
        return self.data.pop(0)

    def is_empty(self):
        return not self.data

    def get_top(self):
        return self.data[0]

    def __str__(self):
        return str(self.data)
