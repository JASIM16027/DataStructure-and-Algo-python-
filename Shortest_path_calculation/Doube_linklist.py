class Node:
    def __init__(self, value):
        self.next = None
        self.prev = None
        self.val = value


class DoubleLinkList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, val):
        node = Node(val)
        if self.tail is None:
            self.head = node
            self.tail = node
            self.size += 1
        else:
            self.tail.next = node
            node.prev = self.head
            self.tail = node
            self.size += 1

    def __remove_node(self, node):
        if node.prev is None:
            self.head = node.next

        if node.next is None:
            self.tail = node.prev

        node.prev.next = node.next
        node.next.prev = node.prev

    def remove(self, value):
        node = self.head
        while node is not None:
            if node.val == value:
                self.__remove_node(node)
            node = node.next

    def __str__(self):
        vals = []
        node = self.head
        while node is not None:
            vals.append(node.val)
            node = node.next
        return f"[{','.join(str(val) for val in vals)}]"


mylist = DoubleLinkList()
mylist.add(1)
mylist.add(3)
mylist.add(5)
mylist.add(8)
mylist.add(10)
print(mylist)

mylist.remove(1)


print(mylist)
