inf=99999
class Graph():
	
	def __init__(self, vertices):
		self.V = vertices
		self.graph = [[0 for column in range(vertices)]
					for row in range(vertices)]

	def printTable(self, dist):
		print("Vertex\tDistance(from S)")
		for node in range(self.V):
			print(node,"\t", dist[node])

	def printPath(self, parent, j):
		if (parent[j]==-1):
			return
		else:
			self.printPath(parent, parent[j])
			print("->",j,end=" ")
	def getMinDistance(self, dist, sptSet):
		minVal = inf
		for u in range(self.V):
			if dist[u] < minVal and sptSet[u] == 0:
				minVal = dist[u]
				min_index = u
		return min_index

	def dijkstra(self, src):
		parent = [-1] * self.V
		dist = [inf] * self.V
		dist[src] = 0
		sptSet = [0] * self.V

		for _ in range(self.V):
			x = self.getMinDistance(dist, sptSet)
			sptSet[x] = 1
			for y in range(self.V):
				if self.graph[x][y] > 0 and sptSet[y] == 0 and dist[y] > dist[x] + self.graph[x][y]:
					dist[y] = dist[x] + self.graph[x][y]
					parent[y] = x

		self.printTable(dist)
		print('\n\n')
		print(0,end=" ")
		self.printPath(parent,5)

	def aSearch(self, src, tgt, hValues):
		def search(currPath, currDist, currHval, held):
			currNode=currPath[-1]
			if currNode==tgt:
				minHval=inf
				for path, dist, hVal in held:
					if hVal < minHval:
						minHval = hVal
						minTemp = (path, dist, hVal)
				if minHval < currHval:
					held.remove(minTemp)
					search(minTemp[0], minTemp[1], minTemp[2], held)
				else:
					print("hValue: ", currHval)
					print(currPath[0], end=" ")
					for i in currPath[1:]:
						print('->', i, end=" ")
			else:
				minHval=inf
				for i in range(self.V):
					if self.graph[currNode][i]>0 and i not in currPath:
						hVal=currDist+self.graph[currNode][i]+hValues[i]
						temp=(currPath+[i], currDist+self.graph[currNode][i], hVal)
						if hVal<minHval:
							minHval=hVal
							minTemp=tuple(temp)
						held.append(temp)
				held.remove(minTemp)
				search(minTemp[0],minTemp[1],minTemp[2], held)
		search([src], 0, 0, [])



if __name__ == "__main__":
	g = Graph(6)
	g.graph = [[0,2,0,4,0,0],
		[2,0,8,15,5,0],
		[0,8,0,2,8,8],
		[4,15,2,0,2,0],
		[0,5,8,0,0,11],
		[0,0,8,0,11,0]]
	
	



	print('Using A* Search\n------------------\n')
	g.aSearch(0, 5, [0,10,16,9,9,0])
	print('\n\nUsing Dijkstra\n------------------\n')
	g.dijkstra(0)



