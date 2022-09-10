class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if self.left is None:
                self.left = Node(data)
            elif self.right is None:
                self.right = Node(data)
            else:
                self.left.insert(data)
        else:
            self.data = data

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()


# Use the insert method to add nodes
root = Node(1)
root.insert(3)
root.insert(5)
root.insert(7)
root.insert(9)
root.insert(11)
root.PrintTree()
