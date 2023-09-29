from collections import deque

class Graph:
    def __init__(self,Nodes,isDirected=False):
        self.nodes=Nodes
        self.adj_list={}
        self.isDirected=isDirected

        for node in Nodes:
            self.adj_list[node]=[]

    
    def add_edge(self,u,v):
        if not self.isDirected:
            self.adj_list[u].append(v)
            self.adj_list[v].append(u)
        else:
            self.adj_list[u].append(v)

    def printGraph(self):

        for key,val in self.adj_list.items():
            print(key,"->",val)


    def bfs(self,node):
        q=deque()

        q.append(node)
        visited=set()
        visited.add(node)

        while q:
            x=q.popleft()
            print(x)

            for neighbour in self.adj_list[x]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    q.append(neighbour)
        

    def dfs(self,node):
        pass


    


l=[1,2,3,4,5]

g=Graph(l)

g.add_edge(1,3)
g.add_edge(2,3)
g.add_edge(3,4)
g.add_edge(1,5)
g.add_edge(5,2)

g.printGraph()

print("bfs")
g.bfs(1)

    