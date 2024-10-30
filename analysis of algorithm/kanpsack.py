def knapsack(weights, values, capacity):
    n = len(weights)
    knapsack_matrix = [[0] * (capacity + 1) for _ in range(n)]
    for i in range(n):
        for w in range(capacity + 1):
            if weights[i] > w:
                knapsack_matrix[i][w] = knapsack_matrix[i - 1][w]
            else:
                knapsack_matrix[i][w] = max(knapsack_matrix[i - 1][w], 
                                             values[i] + knapsack_matrix[i - 1][w - weights[i]])

    # Backtrack to find the items selected
    selected = []
    w = capacity
    for i in range(n - 1, -1, -1):
        if i == 0 and knapsack_matrix[i][w] > 0:
            selected.append(1)
        elif knapsack_matrix[i][w] != knapsack_matrix[i - 1][w]:
            selected.append(1)
            w -= weights[i]
        else:
            selected.append(0)

    selected.reverse()

    return knapsack_matrix, selected

if __name__ == "__main__":
    print("Enter the number of items: ")
    n = int(input())

    weights = []
    values = []

    print("\nEnter the weights of the items: ")
    weights = list(map(int, input().split()))

    print("\nEnter the values of the items: ")
    values = list(map(int, input().split()))

    print("\nEnter the capacity of the knapsack: ")
    capacity = int(input())

    knapsack_matrix, selected = knapsack(weights, values, capacity)

    total_profit = knapsack_matrix[-1][-1]

    print("\nKnapsack Matrix:")
    for row in knapsack_matrix:
        print(row)

    print("\nResultant Vector:")
    print(selected)

    print("\nTotal Profit:", total_profit)

    print("\nObjects Selected:")
    for i, item in enumerate(selected):
        if item:
            print(f"Item {i + 1} (Weight: {weights[i]}, Value: {values[i]})")




def knapsack(weights, values, capacity):
    n = len(weights)
    knapsack_matrix = [[0] * (capacity + 1) for _ in range(n)]
    for i in range(n):
        for w in range(capacity + 1):
            if weights[i] > w:
                knapsack_matrix[i][w] = knapsack_matrix[i - 1][w]
            else:
                knapsack_matrix[i][w] = max(knapsack_matrix[i - 1][w], 
                                             values[i] + knapsack_matrix[i - 1][w - weights[i]])

    # Backtrack to find the items selected
    selected = []
    w = capacity
    for i in range(n - 1, -1, -1):
        if i == 0 and knapsack_matrix[i][w] > 0:
            selected.append(1)
        elif knapsack_matrix[i][w] != knapsack_matrix[i - 1][w]:
            selected.append(1)
            w -= weights[i]
        else:
            selected.append(0)

    selected.reverse()

    return knapsack_matrix, selected


if __name__ == "__main__":
    print("Enter the number of items: ")
    n = int(input())

    weights = []
    values = []

    print("\nEnter the weights of the items: ")
    weights = list(map(int, input().split()))

    print("\nEnter the values of the items: ")
    values = list(map(int, input().split()))

    print("\nEnter the capacity of the knapsack: ")
    capacity = int(input())

    knapsack_matrix, selected = knapsack(weights, values, capacity)

    total_profit = knapsack_matrix[-1][-1]

    print("\nKnapsack Matrix:")
    for row in knapsack_matrix:
        print(row)

    print("\nResultant Vector:")
    print(selected)

    print("\nTotal Profit:", total_profit)

    print("\nObjects Selected:")
    for i, item in enumerate(selected):
        if item:
            print(f"Item {i + 1} (Weight: {weights[i]}, Value: {values[i]})")



