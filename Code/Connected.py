from collections import defaultdict
   
class cGraph:
    def __init__(self,vertices):
        self.V= vertices 
        self.graph = defaultdict(list) 
   
    def addEdge(self,u,v):
        self.graph[u].append(v)
   
    def util(self,v,visited):
        l = []
        visited[v]= True
        #print(chr(v+65))
        l.append((chr(v+65)))
        for i in self.graph[v]:
            if visited[i]==False:
                l.append(self.util(i,visited))
        return l
  
  
    def fillOrder(self,v,visited, stack):
        visited[v]= True
        for i in self.graph[v]:
            if visited[i]==False:
                self.fillOrder(i, visited, stack)
        stack = stack.append(v)
      
  

    def getTranspose(self):
        g = cGraph(self.V)

        for i in self.graph:
            for j in self.graph[i]:
                g.addEdge(j,i)
        return g
  
   
   
    def printSCCs(self):
          
        stack = []
        visited =[False]*(self.V)
        for i in range(self.V):
            if visited[i]==False:
                self.fillOrder(i, visited, stack)
        gr = self.getTranspose()

        visited =[False]*(self.V)
        l = []
        while stack:
            i = stack.pop()
            if visited[i]==False:
                l.append(gr.util(i, visited))
        print(l)
               