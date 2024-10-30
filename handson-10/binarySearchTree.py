class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)
        # Ignore if value already exists in the tree

    def query(self, value):
        return self._query_recursive(self.root, value)

    def _query_recursive(self, node, value):
        if node is None:
            return False
        elif node.value == value:
            return True
        elif value < node.value:
            return self._query_recursive(node.left, value)
        else:
            return self._query_recursive(node.right, value)

    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        if node is None:
            print("Value", value, "not present in the tree.")
            return node

        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Node with two children: Get the inorder successor (smallest in the right subtree)
            temp = self._min_value_node(node.right)
            # Copy the inorder successor's content to this node
            node.value = temp.value
            # Delete the inorder successor
            node.right = self._delete_recursive(node.right, temp.value)

        return node

    def _min_value_node(self, node):
        current = node
        # Find the leftmost leaf node
        while current.left is not None:
            current = current.left
        return current

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.value, end=" ")
            self.inorder_traversal(node.right)

# Function to perform operations based on user input
def perform_operations(bst):
    while True:
        print("\nBinary Search Tree Operations:")
        print("1. Insert")
        print("2. Delete")
        print("3. Query")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            value = int(input("Enter the value to insert: "))
            bst.insert(value)
            print("Value", value, "inserted into the tree.")
        elif choice == '2':
            value = int(input("Enter the value to delete: "))
            if bst.query(value):
                bst.delete(value)
                print("Value",value,"is deleted")
            else:
                print("Value", value, "is not present in the tree.")
        elif choice == '3':
            value = int(input("Enter the value to query: "))
            if bst.query(value):
                print("Value", value, "is present in the tree.")
            else:
                print("Value", value, "is not present in the tree.")
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    bst = BinarySearchTree()
    perform_operations(bst)
