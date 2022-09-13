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

    def bfs(self,initial, goal):
        visited={}
        indice={}
        queue=[]
        for i in range(1,self.n+1):
            visited[self.tree[i]]=False
            indice[self.tree[i]]=i
        queue.append(initial)
        visited[initial] = True
        while queue:
            node = queue.pop(0)
            print(node, end=' ')
            if node==goal:
                break
            x=indice[node]
            if self.tree[x*2] != -1 and visited[self.tree[x*2]]==False:
                queue.append(self.tree[x*2])
                visited[self.tree[x*2]]=True
            if self.tree[x*2+1] != -1 and visited[self.tree[x*2+1]]==False:
                queue.append(self.tree[x*2+1])
                visited[self.tree[x*2+1]]=True
        print()
    
    def dfs(self, initial, goal):
        if initial == goal:
            print(goal)
            return
        else:
            print(initial, end=' ')
            x=self.tree.index(initial)
            if self.tree[x*2] != -1:
                self.dfs(self.tree[x*2],goal)
            if self.tree[x*2+1] != -1:
                self.dfs(self.tree[x*2+1],goal)
            



root = Tree(1)
root.insert(3)
root.insert(5)
root.insert(7)
root.insert(9)
root.insert(11)
print('\n\nTree Structure:')
root.printTree()
print('Using BFS:')
root.bfs(1,11)
print('\n\nUsing DFS:')
root.dfs(1,11)