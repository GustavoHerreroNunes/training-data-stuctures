class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    def __str__(self):
        return str(self.data)


class NodeStack:
    def __init__(self):
        self.top = None
        self.length = 0

    def _set_initial_length(self, current_node):
        if current_node is not None:
            self.length += 1
            self._set_initial_length(current_node.next_node)

    def stack_up(self, node):
        if self.top is None:
            self.top = node
            self._set_initial_length(self.top)
        else:
            node.next_node = self.top
            self.top = node
            self.length += 1

    def unstack(self):
        node = self.top
        self.top = self.top.next_node
        self.length -= 1
        return node

    def is_empty(self):
        return self.top is not None

    def __str__(self):
        if self.top is not None:
            str_stack = f"['{self.top}'"
            current_node = self.top.next_node

            while current_node is not None:
                str_stack += f" ,{current_node}"
                current_node = current_node.next_node

            str_stack += "]"
            return str_stack
        return "[]"
