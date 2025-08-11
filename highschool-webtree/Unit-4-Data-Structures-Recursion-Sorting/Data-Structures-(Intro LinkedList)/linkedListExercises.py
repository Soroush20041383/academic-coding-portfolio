import random

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = Node(data)

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end="")
            if current_node.next:
                print(" -> ", end="")
            else:
                print()  # print a new line at the end of the list
            current_node = current_node.next

    def delete_node_at_distance(self, distance):
        if distance == 0:
            if self.head:
                self.head = self.head.next
        else:
            current_node = self.head
            count = 0
            while current_node and count < distance - 1:
                current_node = current_node.next
                count += 1
            if current_node and current_node.next:
                current_node.next = current_node.next.next

myLL = LinkedList()

# Inserting 20 random integers into the linked list
for _ in range(20):
    myLL.insert(random.randint(1, 100))

myLL.print_list()

# Deleting a node at a certain distance from the head
myLL.delete_node_at_distance(5)

myLL.print_list()
