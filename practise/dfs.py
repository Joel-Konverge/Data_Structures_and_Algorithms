class Adjacent_list:
    def __init__(self):
        self.graph={}
        self.visited=set()
    def add_node(self,n):
        if n not in self.graph:
            self.graph[n]=[]
    def add_edge(self,n1,n2,weight=None):
        if n1 and n2 in self.graph:
            if weight:
                self.graph[n1].append([n2,weight])
            else:
                self.graph[n1].append(n2)
    def dfs(self,n):
        if n not in self.visited:
            print(n , end=" ")
            self.visited.add(n)
            for i in self.graph[n]:
                self.dfs(i)
            

al=Adjacent_list()
al.add_node('5')
al.add_node('3')
al.add_node('7')
al.add_node('2')
al.add_node('4')
al.add_node('8')
al.add_edge('5','3')
al.add_edge('5','7')
al.add_edge('3','2')
al.add_edge('3','4')
al.add_edge('7','8')
al.add_edge('4','8')
al.dfs('5')