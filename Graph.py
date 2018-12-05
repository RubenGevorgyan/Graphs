class AdjMatrix:

    def __init__ (self):
        self.count=int(raw_input("How many people do you want to be?"))
        self.matrix =[]
        self.matrix.append([])
        self.matrix[0].append("/")
        for i in range (1,self.count+1):
            temp=raw_input("What is person name?")
            self.matrix[0].append(temp)
            self.matrix.append([])
            self.matrix[i].append(temp)

    def relativness(self):
        for i in range (1,self.count+1):
            for j in range(1,self.count+1):
                self.matrix[i].append(raw_input("Is "+self.matrix[i][0]+" relative to "+ self.matrix[0][j] +" ?: Yes:1||No:0 \n"))

    def printmatrix(self):
        for i in range (0,self.count+1):
            print(self.matrix[i])


class Graph:
    def __init__(self):
        self.graph1 = {
            'A': ['B', 'S'],
            'B': ['A'],
            'C': ['D', 'E', 'F', 'S'],
            'D': ['C'],
            'E': ['C', 'H'],
            'F': ['C', 'G'],
            'G': ['F', 'S'],
            'H': ['E', 'G'],
            'S': ['A', 'C', 'G']
        }

    def dfs(self, node, visited):
        if node not in visited:
            visited.append(node)
            for n in self.graph1[node]:
                self.dfs( n, visited)
        return visited

    def bfs(self,start):
        explored = []
        queue = [start]

        levels = {}
        levels[start] = 0

        visited = [start]
        while queue:
            node = queue.pop(0)
            explored.append(node)
            neighbours = self.graph1[node]

            for neighbour in neighbours:
                if neighbour not in visited:
                    queue.append(neighbour)
                    visited.append(neighbour)

                    levels[neighbour] = levels[node] + 1
        return visited
def main():
    a=AdjMatrix()
    a.relativness()
    a.printmatrix()
    b=Graph()
    visited=b.dfs('A',[])
    print("This is Depth First")
    print(visited)
    visited=b.bfs('A')
    print("This is Broadth First")
    print(visited)

main()
