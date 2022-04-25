'''
Graph Representation: Generally, a graph is represented as a pair of sets (V, E). V is the set of vertices or nodes. E is the set of Edges. In the above example,
V = { A, B, C, D, E }
E = { AB, AC, AD, BE, CD, DE }

Node or Vertex: The elements of a graph are connected through edges.

Edges: A path or a line between two vertices in a graph.

Adjacent Nodes: Two nodes are called adjacent if they are connected through an edge. Node A is adjacent to nodes B, C, and D in the above example, but not to node E.

Path: Path is a sequence of edges between two nodes. It is essentially a traversal starting at one node and ending at another. Thus, in the example above, there are multiple paths from node A to node E.

Path(A, E) = { AB, BE }
OR
Path(A, E) = { AC, CD, DE }
OR
Path(A, E) = { AD, DE }

Undirected Graph: An undirected graph is one where the edges do not specify a particular direction. The edges are bi-directional.The maximum number of edges possible in an undirected graph without a loop is n×(n-1)/2.

Directed Graph: A directed graph is one where the edges can be traversed in a specified direction only.

Weighted Graph: A weighted graph is one where the edges are associated with a weight. This is generally the cost to traverse the edge.

Unweighted Graph: An unweighted graph does not have any value (weight) associated with every edge in the graph. In other words, an unweighted graph is a weighted graph with all edge weight as 1. Unless specified otherwise, all graphs are assumed to be unweighted by default.

Complete Graph: A complete graph is one in which every two vertices are adjacent: all edges that could exist are present.

Connected Graph: A Connected graph has a path between every pair of vertices. In other words, there are no unreachable vertices. A disconnected graph is a graph that is not connected.

Adjacency Matrix Representation:

An adjacency matrix is a square matrix used to represent a finite graph. The elements of the matrix indicate whether pairs of vertices are adjacent or not in the graph.To store dense graph

Definition:

For a simple unweighted graph with vertex set V, the adjacency matrix is a square |V| × |V| matrix A such that its element:

Aij = 1, when there is an edge from vertex i to vertex j, and
Aij = 0, when there is no edge.

Adjacency List: An adjacency list representation for the graph associates each vertex in the graph with the collection of its neighboring vertices or edges, i.e., every vertex stores a list of adjacent vertices. There are many variations of adjacency list representation depending upon the implementation. This data structure allows the storage of additional data on the vertices but is practically very efficient when the graph contains only a few edges. i.e. the graph is sparse.


'''

# Adjacency Matrix Representation

class Adjacent_matrix:
    def __init__(self):
        self.node=[]
        self.matrix=[]
        self.count=0
    def add_node(self,n):
        if n not in self.node:
            self.count+=1
            self.node.append(n)
        for i in self.matrix:
            i.append(0)
        self.matrix.append([0]*self.count)
        print(self.node)
        print(self.matrix)
    def add_edge_undirected(self,n1,n2,weight=1):
        if n1 and n2 in self.node:
            i1=self.node.index(n1)
            i2=self.node.index(n2)
            self.matrix[i1][i2]=weight
            self.matrix[i2][i1]=weight
            print(self.matrix)
    def add_edge_directed(self,n1,n2,weight=1):
        if n1 and n2 in self.node:
            i1=self.node.index(n1)
            i2=self.node.index(n2)
            self.matrix[i1][i2]=weight
            print(self.matrix)
        
    def delete_node(self,n):
        if n in self.node: 
            idx=self.node.index(n)    
            self.node.remove(n)
            self.matrix.pop(idx)
            for i in self.matrix:
                i.pop(idx)
            self.count-=1
            print(self.node)
            print(self.matrix)

    def delete_edge_undirected(self,n1,n2):
        if n1 and n2 in self.node:
            idx1=self.node.index(n1) 
            idx2=self.node.index(n2) 
            self.matrix[idx1][idx2]=0
            self.matrix[idx2][idx1]=0
            print(self.matrix)

    def delete_edge_directed(self,n1,n2):
        if n1 and n2 in self.node:
            idx1=self.node.index(n1) 
            idx2=self.node.index(n2) 
            self.matrix[idx1][idx2]=0
            print(self.matrix)


am=Adjacent_matrix()
am.add_node("A")
am.add_node("B")
am.add_node("C")
am.add_node("D")
am.add_edge_undirected("A","B")
print("delete")
am.delete_node("C")
# am.delete_edge_undirected("A","B")
am.delete_edge_directed("A","B")
# am.add_edge_directed("A","B",5)





# Adjacency List Representation

class Adjacent_list:
    def __init__(self):
        self.graph={}
    def add_node(self,n):
        if n not in self.graph:
            self.graph[n]=[]
            print(self.graph)
    def add_edge_undirected(self,n1,n2,weight=None):
        if n1 and n2 in self.graph:
            if weight:
                self.graph[n1].append([n2,weight])
                self.graph[n2].append([n1,weight])
            else:
                self.graph[n1].append(n2)
                self.graph[n2].append(n1)
            print(self.graph)
    def add_edge_directed(self,n1,n2,weight=None):
        if n1 and n2 in self.graph:
            if weight:
                self.graph[n1].append([n2,weight])
            else:
                self.graph[n1].append(n2)
            print(self.graph)

    def delete_node(self,n):
        if n in self.graph:
            self.graph.pop(n)
            for i in self.graph:
                l=self.graph[i]
                try:
                    if isinstance (l[0],list):
                        for j in l:
                            if n==j[0]:
                                l.remove(j)
                                break
                except:
                    if n in l:
                        l.remove(n)
        print(self.graph)
    
    def delete_edge_undirected(self,n1,n2,weight=1):
        if n1 and n2 in self.graph:
            if isinstance(self.graph[n1][0],list):
                if [n2,weight] in self.graph[n1]:
                    self.graph[n2].remove([n1,weight] )
                    self.graph[n1].remove([n2,weight] )
            elif n2 in self.graph[n1]:
                self.graph[n1].remove(n2)
                self.graph[n2].remove(n1)
        print(self.graph)

    def delete_edge_directed(self,n1,n2,weight=1):
        if n1 and n2 in self.graph:
            if isinstance(self.graph[n1][0],list):
                if [n2,weight] in self.graph[n1]:
                    self.graph[n1].remove([n2,weight])
            elif n2 in self.graph[n1]:
                self.graph[n1].remove(n2)
        print(self.graph)



al=Adjacent_list()
al.add_node("A")
al.add_node("B")
al.add_node("C")
# al.add_edge_undirected("A","B")
al.add_edge_undirected("A","B",4)
print("Delete")
# al.delete_edge_undirected("A","B",4)
al=Adjacent_list()
al.add_node("A")
al.add_node("B")
al.add_node("C")
# al.add_edge_directed("A","B")
al.add_edge_directed("A","C",4)
print("Delete")
al.delete_edge_directed("A","C",4)