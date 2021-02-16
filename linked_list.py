# How to create a linked list

class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

        def __str__(self):
            return self.data

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)


llist = LinkedList()
first_node = Node("a")
second_node = Node("b")
llist.head = first_node
first_node.next = second_node
print(llist)


second_node = Node("b")
third_node = Node("c")
first_node.next = second_node
second_node.next = third_node
print(llist)