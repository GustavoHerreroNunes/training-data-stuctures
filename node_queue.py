class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    def __str__(self):
        return str(self.data)


class NodeQueue:
    def __init__(self):
        self.first = None
        self.length = 0

    def _set_initial_length(self, current_node):
        if current_node is not None:
            self.length += 1
            self._set_initial_length(current_node.next_node)

    def queue(self, node):
        if self.first is None:
            self.first = node
            self._set_initial_length(self.first)
        else:
            if self.first.next_node is None:
                self.first.next_node = node
            else:
                last = self.get_last_node(self.first)
                last.next_node = node
            self.length += 1

    def dequeue(self):
        if self.first is None:
            return None
        node = self.first
        self.first = self.first.next_node
        return node

    def get_last_node(self, current_node):
        if current_node.next_node is None:
            return current_node
        return self.get_last_node(current_node.next_node)

    def is_empty(self):
        return self.first is not None

    def __str__(self):
        if self.first is not None:
            str_queue = f"['{self.first}'"
            current_node = self.first.next_node

            while current_node is not None:
                str_queue += f" ,{current_node}"
                current_node = current_node.next_node

            str_queue += "]"
            return str_queue
        return "[]"
