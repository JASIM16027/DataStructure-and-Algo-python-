class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def largest(root):
    if root is None:
        return -1 ##tree has no node
    return max(root.data,largest(root.left),largest(root.right))
bt1=BinaryTreeNode(1)
bt2=BinaryTreeNode(2)
bt3=BinaryTreeNode(3)
bt4=BinaryTreeNode(7)
bt5=BinaryTreeNode(9)
bt6=BinaryTreeNode(3)
bt7=BinaryTreeNode(31)
bt1.left=bt2
bt1.right=bt3
bt2.left=bt4
bt2.right=bt5
bt3.left=bt6
bt3.right=bt7
print(largest(bt1))