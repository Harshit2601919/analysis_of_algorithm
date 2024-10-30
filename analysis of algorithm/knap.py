def knapsack(weight,values,capacity):
    n=len(weight)
    knapsack_matrix=[[0]*(capacity+1) for _ in range(n)]
    for i in range(n):
        for w in range(capacity+1):
            if weight[i]>w:
                knapsack_matrix[i][w]=knapsack_matrix[i-1][w]

            else:
                knapsack_matrix[i][w]=max(knapsack_matrix[i-1][w],values[i]+knapsack_matrix[i-1][w-weight
                                                                                                 
                                                                                                 [i]])
    selected=[]
    w=capacity
    for i in range(n-1,-1,-1):
        if i==0 and knapsack_matrix[i-1][w]>0:
            selected.append(1)
        elif knapsack_matrix[i][w]!=knapsack_matrix[i-1][w]:
            selected.append(1)
            w-=weight[i]
        else:
            selected.append(0)

    selected.reverse()
    return knapsack_matrix,selected



if __name__=="__main__":
    