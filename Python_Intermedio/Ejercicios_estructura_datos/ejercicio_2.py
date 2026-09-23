class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class Deque:
    def __init__(self):
        self.left = None
        self.right = None

    def push_left(self, value):
        new_node = Node(value)

        if self.left is None:
            self.left = new_node
            self.right = new_node
        else:
            new_node.next = self.left
            self.left.prev = new_node
            self.left = new_node

    def push_right(self, value):
        new_node = Node(value)

        if self.right is None:
            self.left = new_node
            self.right = new_node
        else:
            new_node.prev = self.right
            self.right.next = new_node
            self.right = new_node

    def pop_left(self):
        if self.left is None:
            raise Exception("La estructura está vacía")

        value = self.left.value
        self.left = self.left.next

        if self.left is None:
            self.right = None
        else:
            self.left.prev = None

        return value

    def pop_right(self):
        if self.right is None:
            raise Exception("La estructura está vacía")

        value = self.right.value
        self.right = self.right.prev

        if self.right is None:
            self.left = None
        else:
            self.right.next = None

        return value

    def print_deque(self):
        current = self.left

        while current is not None:
            print(current.value)
            current = current.next


deque = Deque()

deque.push_right(10)
deque.push_right(20)
deque.push_left(5)
deque.push_left(1)

print("Deque:")
deque.print_deque()

print("Pop left:", deque.pop_left())
print("Pop right:", deque.pop_right())

print("Deque después de los pop:")
deque.print_deque()