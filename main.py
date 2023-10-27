from simple_linked_list import Node as Simple_Node, SimpleLinkedList
from doubly_linked_list import Node as Doubly_Node, DoublyLinkedList
from simple_stack import Stack as SimpleStack
from node_stack import Node as Stack_Node, NodeStack
from simple_queue import Queue as SimpleQueue
from node_queue import Node as Queue_Node, NodeQueue

if __name__ == '__main__':
    defaultNode = [
        "The Journey", "The Last of Us", "Horizon: Forbidden West",
        "Little Nightmares", "Father and Son", "Angry Birds 2"
    ]

    simple_list = SimpleLinkedList()
    doubly_list = DoublyLinkedList()
    simple_stack = SimpleStack()
    node_stack = NodeStack()
    simple_queue = SimpleQueue()
    node_queue = NodeQueue()

    for node in defaultNode:
        simple_list.add_node(Simple_Node(node))
        doubly_list.add_node(Doubly_Node(node))
        simple_stack.stack_up(node)
        node_stack.stack_up(Stack_Node(node))
        simple_queue.queue(node)
        node_queue.queue(Queue_Node(node))

    print("\nBem vinde à demonstração de estruturas de dados!")

    selected_menu_option = -1
    while selected_menu_option != 6:
        print("\nMenu de opções:")
        print("\n0 - Lista Encadeada Simples")
        print("1 - Lista Duplamente Encadeada")
        print("2 - Pilha Simples")
        print("3 - Pilha Nodular")
        print("4 - Fila Simples")
        print("5 - Fila Nodular")
        print("6 - Sair")
        selected_menu_option = int(input("\nDigite um número para selecionar uma opção:\n"))

        match selected_menu_option:
            case 0:
                print("Simple Linked List")
                print("========================\n")
                print(f"[last_node]: {simple_list.get_last_node(simple_list.head)}")
                print(f"[simple_list]: {simple_list}")
                print(f"simple_list.contains('The Last of Us'): "
                      f"{simple_list.contains_node(simple_list.head, 'The Last of Us')}")
                print(f"simple_list.contains('Horizon: Zero Dawn'): "
                      f"{simple_list.contains_node(simple_list.head, 'Horizon: Zero Dawn')}")
                print(f"simple_list.contains('Little Nightmares'): "
                      f"{simple_list.contains_node(simple_list.head, 'Little Nightmares')}")
                print(f"simple_list.delete('The Last of Us'): "
                      f"{simple_list.delete_node(simple_list.head, 'The Last of Us')}")
                print(f"simple_list.delete('The Journey'): "
                      f"{simple_list.delete_node(simple_list.head, 'The Journey')}")
                print(f"[simple_list]: {simple_list}")
            case 1:
                print("Doubly Linked List")
                print("========================\n")
                print(f"[doubly_list]: {doubly_list}")
                print(f"[head]: {doubly_list.head}")
                print(f"doubly_list.contains('The Last of Us'): "
                      f"{doubly_list.contains_node('The Last of Us', doubly_list.head, doubly_list.tail)}")
                print(f"doubly_list.contains('Horizon: Zero Dawn'): "
                      f"{doubly_list.contains_node('Horizon: Zero Dawn', doubly_list.head, doubly_list.tail)}")
                print(f"doubly_list.delete('The Last of Us'): "
                      f"{doubly_list.delete_node('The Last of Us', doubly_list.head, doubly_list.tail)}")
                print(f"doubly_list.delete('The Journey'): "
                      f"{doubly_list.delete_node('The Journey', doubly_list.head, doubly_list.tail)}")
                print(f"[doubly_list]: {doubly_list}")
            case 2:
                print("Simple Stack")
                print("========================\n")
                print(f"[simple_stack]: {simple_stack}")
                print(f"[simple_stack.unstack()]: {simple_stack.unstack()}")
                print(f"[simple_stack]: {simple_stack}")
                print(f"[simple_stack.top]: {simple_stack.get_top()}")
            case 3:
                print("Node Stack")
                print("========================\n")
                print(f"[node_stack]: {node_stack}")
                print(f"[node_stack.unstack()]: {node_stack.unstack()}")
                print(f"[node_stack]: {node_stack}")
                print(f"[node_stack.length]: {node_stack.length}")
            case 4:
                print("Simple Queue")
                print("========================\n")
                print(f"[simple_queue]: {simple_queue}")
                print(f"[simple_queue.length]: {simple_queue.length}")
                print(f"[simple_queue.unstack()]: {simple_queue.dequeue()}")
                print(f"[simple_queue]: {simple_queue}")
                print(f"[simple_queue.length]: {simple_queue.length}")
                print(f"[simple_queue.top]: {simple_queue.get_first()}")
            case 5:
                print("Node Queue")
                print("========================\n")
                print(f"[node_queue]: {node_queue}")
                print(f"[node_queue.length]: {node_queue.length}")
                print(f"[node_queue.unstack()]: {node_queue.dequeue()}")
                print(f"[node_queue]: {node_queue}")
                print(f"[node_queue.length]: {node_queue.length}")
                print(f"[node_queue.last]: {node_queue.get_last_node(node_queue.first)}")
            case 6:
                print("Encerrando programa, volte sempre :)")
            case _:
                print("Este número não correponde a nenhuma opção do menu :(")
