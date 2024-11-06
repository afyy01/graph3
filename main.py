class Graph: #undirected graph
    def __init__(self,V):
        self.V = V
        self.adj = [[] for i in range(V)]

    def DFS(self,temp,v,visited):
        #mark the correct node as visited
        visited[v]=True
        #store the node to the list
        temp.append(v)

        #repeat the process for all the adjacent nodes
        for i in self.adj[v]:
            if visited[i] == False:
                #update the list
                temp = self.DFS(temp,i,visited)
        
        return temp
    
    def add_edge(self,v,w):
        self.adj[v].append(w)
        self.adj[w].append(v)

    #method for retreiving the connected components in undirected graph
    def ConnectedComponents(self):
        visited = []
        cc = []
        for i in range(self.V):
            visited.append(False)
        for v in range(self.V):
            if visited[v] == False:
                temp = []
                cc.append(self.DFS(temp,v,visited))
        
        return cc
    
g = Graph(5)
g.add_edge(0,3)
g.add_edge(2,3)
g.add_edge(3,4)


print(g)

cc = g.ConnectedComponents()
print("The connected components are: ")
print(cc)