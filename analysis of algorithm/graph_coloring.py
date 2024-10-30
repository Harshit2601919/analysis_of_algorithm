def is_safe(vertex,graph,color,c):
    for i in range(len(graph)):
        if graph[vertex][i]==1 and color[i]==c:
            return False
        
    return True


def graph_coloring(graph,num_colors):
    n=len(graph)
    colors=[0]*n
    solutions=[]

    def backtrack(vertex):
        if vertex==n:
            solutions.append(colors[:])
            return True
        

        for c in range(1,num_colors+1):
            if is_safe(vertex,graph,colors,c):
                colors[vertex]=c
                backtrack(vertex+1)
                colors[vertex]=0

    backtrack(0)
    return solutions

if __name__=="__main__":
    n=int(input("enter the number of vertices"))

    print("enter the adjacency matrix")
    graph=[]
    for _ in range(n):
        row=list(map(int,input().strip().split()))
        graph.append(row)

    num_colors=int(input("enter the number of the colors"))
    solutions=graph_coloring(graph,num_colors)
    print("all the possible solution is ")
    for i,solution in enumerate(solutions):
        print(f"solution is {i+1}:{solution}")


def is_safe(vertex,graph,color,c):
    for i in range(len(graph)):
        if graph[vertex][i]==1 and color[i]==c:
            return False
        
    return True


def graph_color(graph,num_color):
    n=len(graph)
    color=[0]*n
    solution=[]
    def backtrack(vertex):
        if vertex==n:
            solution.append(color[:])
            return True

    
        for c in range(1,num_color+1):
          if is_safe(vertex,graph,color,c):
              color[vertex]==c
              backtrack(vertex+1)
              color[vertex]=0

    backtrack(0)
    return solution         


if __name__=="__main__":
    n=int(input("enter the number of vertex"))

    graph=[]
    print("enter the adjanecy matrix")
    for row in range(n):
        temp=int(input().split())
        graph.append(temp)
    num_color=int(input("enter the maximum color to be used"))
    solution=graph_color(graph,num_color)
    for i,solutions in enumerate(solution):
        print(f"solution is ")
                   