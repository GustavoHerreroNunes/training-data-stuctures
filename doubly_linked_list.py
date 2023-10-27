class Node:
    def __init__(self, data, next_node=None, previous_node=None):
        self.data = data
        self.next_node = next_node
        self.previous_node = previous_node

    def __str__(self):
        return str(self.data)

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, node):
        if self.head is None and self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next_node = node
            node.previous_node = self.tail
            self.tail = node

    def delete_node(self, node_data, start_node, end_node):
        if node_data is None:
            return False
        if start_node == self.head:
            if start_node.data == node_data:
                if start_node.next_node:
                    self.head.next_node.previous_node = None
                    self.head = self.head.next_node
                    return start_node
                else:
                    self.head = None
                    return start_node
        elif end_node == self.tail:
            if end_node.data == node_data:
                if end_node.previous_node:
                    self.tail.previous_node.next_node = None
                    self.tail = self.tail.previous_node
                    return end_node
                else:
                    self.tail = None
                    return end_node
        else:
            if start_node.data == node_data:
                start_node.next_node.previous_node = start_node.previous_node
                start_node.previous_node.next_node = start_node.next_node
                return start_node
            elif end_node.data == node_data:
                end_node.previous_node.next_node = end_node.next_node
                end_node.next_node.previous_node = end_node.previous_node
                return end_node
            elif start_node.previous_node == end_node.next_node or start_node.previous_node == end_node:
                return False
        start_node = start_node.next_node
        end_node = end_node.previous_node
        return self.delete_node(node_data, start_node, end_node)

    def contains_node(self, node_data, start_node, end_node):
        if node_data is None:
            return False
        if (start_node != self.head) and (end_node != self.tail):
            if(start_node.previous_node == end_node.next_node
               or start_node.previous_node == end_node):
                return False
        if start_node.data == node_data or end_node.data == node_data:
            return True
        else:
            start_node = start_node.next_node
            end_node = end_node.previous_node
            return self.contains_node(node_data, start_node, end_node)

    def __str__(self):
        if self.head is not None:
            str = f"['{self.head}'"
            current_node = self.head.next_node
            while current_node is not None:
                str += f", '{current_node}'"
                current_node = current_node.next_node
            str += "]"
            return str
        else:
            return "[]"
