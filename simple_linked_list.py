class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return f"'{self.data}'"


class SimpleLinkedList:
    def __init__(self, head=None):
        self.head = head

    def add_node(self, node):
        if self.head is None:
            self.head = node
        else:
            last_node = self.get_last_node(self.head)
            last_node.next = node

    def get_last_node(self, start_node):
        if start_node.next is None:
            return start_node
        else:
            return self.get_last_node(start_node.next)

    def contains_node(self, current_node, node_data):
        if node_data is None or current_node is None:
            return False
        elif node_data == current_node.data:
            return True
        else:
            return self.contains_node(current_node.next, node_data)

    def delete_node(self, current_node, node_data):
        if node_data is None or current_node is None:
            return False
        elif current_node == self.head and current_node.data == node_data:
            if self.head.next:
                deleted_node = self.head
                self.head = self.head.next
            else:
                deleted_node = self.head
                self.head = None
            return deleted_node
        elif current_node.next:
            if current_node.next.data == node_data:
                deleted_node = current_node.next
                current_node.next = current_node.next.next
                return deleted_node

        return self.delete_node(current_node.next, node_data)

    def __str__(self):
        if self.head is not None:
            str = f"[{self.head}"
            current_node = self.head.next
            while current_node is not None:
                str += f", {current_node}"
                current_node = current_node.next
            str += "]"
            return str
        else:
            return "[]"
