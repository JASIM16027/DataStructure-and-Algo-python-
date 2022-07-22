class Node:
    def __init__(self, data=None, previous=None, next=None):
        self.data = data
        self.previous = previous
        self.next = next

    def __repr__(self):
        return repr(self.data)


class DoublyLinkList:
    def __init__(self):
        self.head = Node()

    def __repr__(self):
        current_node = self.head.next
        nodes = []
        while current_node:
            nodes.append(repr(current_node))
            current_node = current_node.next

        return ','.join(nodes)

    def prepend(self, data):
        node = Node(data)
        if self.head.next is None:
            self.head.next = node
        else:
            node.next = self.head.next
            node.next.previous = node
            self.head.next = node

    def append(self, data):
        node = Node(data)

        if self.head.next is None:
            self.head.next = node
            return

        current_node = self.head.next
        while current_node.next:
            current_node = current_node.next

        current_node.next = node
        node.previous = current_node

    def search(self, item):
        current_node = self.head.next

        while current_node:
            if current_node.data == item:
                return current_node
            current_node = current_node.next
        return None

    def remove_node(self, node):

        if node.previous:
            node.previous.next = node.next
        else:
            self.head.next = node.next
        if node.next:
            node.next.previous = node.previous

    def remove(self, item):
        node = self.search(item)
        if node is None:
            return
        self.remove_node(node)


if __name__ == '__main__':
    dl = DoublyLinkList()
    dl.append(10)
    dl.append(12)
    print(dl)
    dl.prepend(22)
    dl.prepend(23)
    dl.prepend(9)
    print(dl)
    dl.remove(12)
    print(dl)
