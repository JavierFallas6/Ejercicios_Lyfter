class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.head is None:
            raise Exception("El Stack está vacío")

        data = self.head.data
        self.head = self.head.next

        return data

    def print_stack(self):
        current = self.head

        while current is not None:
            print(current.data)
            current = current.next



stack = Stack()


stack.push(10)
stack.push(20)
stack.push(30)

print("Stack:")
stack.print_stack()


print("Pop:", stack.pop())

print("Stack después del pop:")
stack.print_stack()