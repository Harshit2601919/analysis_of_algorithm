def is_safe(graph,vertex,color,c):
    for i in range(len(graph)):
        if graph[vertex][i]==1 and color[i]==c:
            return False
    return True


def graph_coloring(graph,num_color):
    n=len(graph)
    colors=[0]*n
    solutions=[]

    def backtrack(vertex):
        if vertex==n:
            solutions.append(colors[:])

            return True
        
        for c in range(1,num_color+1):
            if is_safe(graph,vertex,colors,c):
                colors[vertex]=c
                backtrack(vertex+1)
                colors[vertex]=0

    backtrack(0)
    return solutions


if __name__=="__main__":
  n=int(input("enter the numbers od elemts "))
  print("enter the adjacency matrix")
  graph=[]
  for _ in range(n):
      temp=list(map(int,input().split()))
      graph.append(temp)

  num_color=int(input("enter the max colors"))
  solutions=graph_coloring(graph,num_color)
  print("the solution is ")
  for i,solution in enumerate(solutions):
      print(f"solution {i+1}",solution)

    

