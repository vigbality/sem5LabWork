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
                if not self.left.isFull() or self.right.isFull():
                    self.left.insert(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def isFull(self):
        if self.left is not None and self.right is not None:
            return True
        else:
            return False

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()


def bfs(initial, goal):
    if initial.data == goal.data:
        print(initial.data)
        return
    else:
        if initial.left is not None:
            if initial.left.data == goal.data:
                print(initial.left.data)
                return
            else:
                print(initial.left.data)
        if initial.right is not None:
            if initial.right.data == goal.data:
                print(initial.right.data)
                return
            else:
                print(initial.right.data)
        if initial.left is not None:
            bfs(initial.left, goal)
        else:
            return


def dfs(initial, goal):
    if initial.data == goal.data:
        print(initial.data)
        return
    else:
        if initial.left is not None:
            if initial.left.data == goal.data:
                print(initial.left.data)
                return
            else:
                print(initial.left.data)
                dfs(initial.left, goal)
        if initial.right is not None:
            if initial.right.data == goal.data:
                print(initial.right.data)
                return
            else:
                print(initial.right.data)
                dfs(initial.right, goal)


# Use the insert method to add nodes
root = Node(1)
root.insert(3)
root.insert(5)
root.insert(7)
root.insert(9)
root.insert(11)
# root.PrintTree()
bfs(root, Node(11))
