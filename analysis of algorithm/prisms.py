def prims(G):
    n = len(G)
    visited = [False] * n
    min_cost = 0
    spanning = [[0] * n for _ in range(n)]
    visited[0] = True

    for _ in range(n - 1):
        min_distance = float('inf')
        u, v = -1, -1

        for i in range(n):
            if visited[i]:
                for j in range(n):
                    if not visited[j] and G[i][j] < min_distance:
                        min_distance = G[i][j]
                        u, v = i, j

        if u != -1 and v != -1:
            spanning[u][v] = min_distance
            spanning[v][u] = min_distance
            visited[v] = True
            min_cost += min_distance

    return spanning, min_cost

if __name__ == "__main__":
    print("Enter number of vertices: ")
    n = int(input())

    print("\nEnter the adjacency matrix:\n")
    G = []
    for _ in range(n):
        row = list(map(int, input().split()))
        G.append(row)

    spanning, total_cost = prims(G)

    print("\nSpanning tree matrix:\n")
    for row in spanning:
        print(' '.join(map(str, row)))

    print("\nTotal cost of spanning tree is:", total_cost)
