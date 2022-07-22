class TreeNode:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None

    def __repr__(self):
        return repr(self.data)

    def add_left(self, node):
        self.left = node
        print("add_left", self.left)
        if node is not None:
            node.parent = self
            print("add_left_parent",node.parent)

    def add_right(self, node):
        self.right = node
        print("add_right", self.right)
        if node is not None:
            node.parent = self
            print("add_right",node.parent)


def bst_search(node, key):
    while node is not None:
        if node.data == key:
            return node
        if key < node.data:
            node = node.left
        else:
            node = node.right
    return node


def bst_insert(root, node):
    last_node = None
    current_node = root

    while current_node is not None:
        last_node = current_node
        if current_node.data > node.data:
            current_node = current_node.left
        else:
            current_node = current_node.right

    if last_node is None:
        root = node
    elif node.data < last_node.data:
        last_node.add_left(node)
    else:
        last_node.add_right(node)
    return root


def create_bst():
    root = TreeNode(10)
    LL = [5, 17, 3, 7, 12, 19, 1, 4, 13]
    for item in LL:
        node = TreeNode(item)
        print(node, end=' ')
        root = bst_insert(root, node)
    return root


def in_order(node):
    if node.left:
        in_order(node.left)
    print(node)

    if node.right:
        in_order(node.right)


def bst_minimun(root):
    while root.left is not None:
        root = root.left

    return root


def bst_transplat(root, current_node, new_node):
    print(root,current_node,new_node)
    if current_node.parent is None:
        root = new_node
        print('root_bst_t', root)
    elif current_node == current_node.parent.left:
        current_node.parent.add_left(new_node)
    else:
        current_node.parent.add_left(new_node)

    return root


def bst_delete(root, node):
    if node.left is None:
        root = bst_transplat(root, node, node.right)
    elif node.right is None:
        root = bst_transplat(root, node, node.left)
    else:
        min_node = bst_minimun(node.right)
        if min_node.parent!= node:
            root = bst_transplat(root, min_node, min_node.right)
            print(min_node)
            min_node.add_right(node.right)
        root = bst_transplat(root, node, min_node)
        print(min_node)
        min_node.add_left(node.left)
    return root


if __name__ == '__main__':
    root = create_bst()
    print("Binary Search Tree : ")
    in_order(root)

    for key in [10]:
        node = bst_search(root, key)
        print("will delete", node)
        root = bst_delete(root, node)
        print('BST : ')
        in_order(root)
