class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root

    # To get Root
    def get_root(self):
        return self.root

    # insertion
    def insert_helper(self, this_node, key):
        if this_node.key < key:
            if this_node.right is None:
                this_node.right = Node(key)
            else:
                self.insert_helper(this_node.right, key)
        elif this_node.key > key:
            if this_node.left is None:
                this_node.left = Node(key)
            else:
                self.insert_helper(this_node.left, key)

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self.insert_helper(self.root, key)

    # searching a key in Binary search tree
    def search(self, this_node, key):
        if this_node is None:
            print('Key not found')
            return False
        elif this_node.key == key:
            print('Key was found')
            return True
        elif key < this_node.key:
            self.search(this_node.left, key)
        else:
            self.search(this_node.right, key)

    # Deletion of Key
    # First Finding Inorder Successor <== Smallest From Right ==>
    def find_inorder_successor(self, this_node):
        my_val = this_node
        while my_val.left is None:
            my_val = my_val.left
        return my_val

    # deleting
    def delete_node(self, this_node, key):
        if this_node is None:
            return this_node
        if key < this_node.key:
            this_node.left = self.delete_node(this_node.left, key)
        elif key > this_node.key:
            this_node.right = self.delete_node(this_node.right, key)
            # case 1 with no child or 1 child
        else:
            if this_node.left is None:
                temp = this_node.right
                this_node = None
                return temp
            elif this_node.right is None:
                temp = this_node.left
                this_node = None
                return temp
            # case 2 with 2 child
            temp = self.find_inorder_successor(this_node.right)
            this_node.key = temp.key
            this_node.right = self.delete_node(this_node.right, temp.key)
        return this_node



    # printing inorder  <== LEFT, ROOT, RIGHT  ==>
    def print_inorder(self, this_node):
        if this_node:
            self.print_inorder(this_node.left)
            print(this_node.key, end=" ")
            self.print_inorder(this_node.right)

    # printing pre order <== ROOT, LEFT, RIGHT ==>
    def print_preorder(self, this_node):
        if this_node:
            print(this_node.key, end=" ")
            self.print_preorder(this_node.left)
            self.print_preorder(this_node.right)

    # printing post order <== LEFT, RIGHT, ROOT ==>
    def print_postorder(self, this_node):
        if this_node:
            self.print_postorder(this_node.left)
            self.print_postorder(this_node.right)

            print(this_node.key, end=" ")

# Driver Code
if __name__ == "__main__":
    bst = BinarySearchTree()
    list = [10, 13, 21, 14, 8, 15, 32, 9]
    for i in list:
        bst.insert(i)
    bst.delete_node(bst.root, 14)
    bst.search(bst.root, 21)
    print("In-Order Traversal")
    bst.print_inorder(bst.root)
    print("\nPre-Order Traversal")
    bst.print_preorder(bst.root)
    print("\nPost-Order Traversal")
    bst.print_postorder(bst.root)
