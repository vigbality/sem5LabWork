from math import log2, floor
class Tree:
    def __init__(self, data):
        self.tree = [-1]*100
        self.tree[1] = data
        self.n = 1

    def insert(self, data):
        self.n+=1
        self.tree[self.n] = data

    def printTree(self):
        i=1
        level=1
        while i<=self.n:
            space=((2**(floor(log2(self.n))))*10)//level
            for _ in range(level):
                if self.tree[i] == -1:
                    break 
                print(str(self.tree[i]).center(space), end='')
                i+=1
            print('\n\n')
            level*=2
        print()


root = Tree(1)
root.insert(3)
root.insert(5)
root.insert(7)
root.insert(9)
root.insert(11)
root.printTree()
