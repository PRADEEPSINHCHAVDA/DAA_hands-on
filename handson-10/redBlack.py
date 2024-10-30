class Node:
    def __init__(self, value, color='red'):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None  # Add parent attribute
        self.color = color


class RedBlackTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value, color='black')
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left:
                self._insert_recursive(node.left, value)
            else:
                new_node = Node(value)
                node.left = new_node
                new_node.parent = node  # Set parent attribute
                self._fix_violation(new_node)
        else:
            if node.right:
                self._insert_recursive(node.right, value)
            else:
                new_node = Node(value)
                node.right = new_node
                new_node.parent = node  # Set parent attribute
                self._fix_violation(new_node)

    def _fix_violation(self, node):
        while node != self.root and node.color != 'black' and node.parent.color == 'red':
            parent = node.parent
            grandparent = parent.parent

            if parent == grandparent.left:
                uncle = grandparent.right

                if uncle and uncle.color == 'red':
                    grandparent.color = 'red'
                    parent.color = 'black'
                    uncle.color = 'black'
                    node = grandparent
                else:
                    if node == parent.right:
                        self.rotate_left(parent)
                        node = parent
                        parent = node.parent
                    self.rotate_right(grandparent)
                    parent.color, grandparent.color = grandparent.color, parent.color
                    node = parent
            else:
                uncle = grandparent.left

                if uncle and uncle.color == 'red':
                    grandparent.color = 'red'
                    parent.color = 'black'
                    uncle.color = 'black'
                    node = grandparent
                else:
                    if node == parent.left:
                        self.rotate_right(parent)
                        node = parent
                        parent = node.parent
                    self.rotate_left(grandparent)
                    parent.color, grandparent.color = grandparent.color, parent.color
                    node = parent

        self.root.color = 'black'

    def rotate_left(self, node):
        right_child = node.right
        node.right = right_child.left

        if node.right:
            node.right.parent = node

        right_child.parent = node.parent

        if not node.parent:
            self.root = right_child
        elif node == node.parent.left:
            node.parent.left = right_child
        else:
            node.parent.right = right_child

        right_child.left = node
        node.parent = right_child

    def rotate_right(self, node):
        left_child = node.left
        node.left = left_child.right

        if node.left:
            node.left.parent = node

        left_child.parent = node.parent

        if not node.parent:
            self.root = left_child
        elif node == node.parent.left:
            node.parent.left = left_child
        else:
            node.parent.right = left_child

        left_child.right = node
        node.parent = left_child

    def _print_tree(self, node, level=0):
        if node:
            self._print_tree(node.right, level + 1)
            print('     ' * level + str(node.value) + ' (' + node.color + ')')
            self._print_tree(node.left, level + 1)

    def print_tree(self):
        self._print_tree(self.root)


# Example usage:
rbt = RedBlackTree()
rbt.insert(10)
rbt.insert(20)
rbt.insert(30)
rbt.insert(40)
rbt.insert(50)
rbt.insert(60)
rbt.insert(70)
rbt.insert(80)
rbt.print_tree()
