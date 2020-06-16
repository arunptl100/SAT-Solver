class node:
    def __init__(self, data, next_node):
        self.data = data
        self.next = next_node

    def show_data(self):
        if self.next is not None:
            print(self.data, end=', ')
        else:
            print(self.data, end='')


class linked_list:
    def __init__(self, initData):
        newNode = node(initData, None)
        self.head = newNode
        self.tail = newNode

    def append(self, data):
        newNode = node(data, None)
        self.tail.next = newNode
        self.tail = newNode

    def print(self):
        node_ptr = self.head
        print("{", end=' ')
        while node_ptr is not None:
            node_ptr.show_data()
            node_ptr = node_ptr.next
        print(" }\n")


ll = linked_list(2)
ll.append(3)
ll.append(6)
ll.append(1)
ll.print()
