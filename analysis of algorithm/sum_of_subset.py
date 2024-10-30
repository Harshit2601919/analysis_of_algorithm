def sum_subsets(s,k,r,w,x,m):
    x[k]=1
    if s+w[k]==m:
        print_solution(x,w)
    elif s+w[k]+w[k+1]<=m:
        sum_subsets(s+w[k],k+1,r-w[k],w,x,m)
    if s+r-w[k]>=m and s+w[k+1]<=m:
        x[k]=0
        sum_subsets(s,k+1,r-w[k],w,x,m)

def print_solution(x,w):
    subset=[w[i] for i in range(len(x)) if x[i]==1]
    print(f"the solution is {tuple(subset)}")
    print("the vector is  [", end=" ")
    for val in w:
        print("1" if val in subset else "0",end=" ")
    print("]")

def generate_subset(w,s):
    n=len(w)
    x=[0]*n
    r=sum(w)
    sum_subsets(0,0,r,w,x,s)

def main():
    n=int(input(" enter the number of elemets:"))
    w=[int(input(f"entee the elemts {i+1}"))for i in range(n)]
    s=int(input("enter the target"))
    w.sort()
    generate_subset(w,s)

if __name__=="__main__":
    main()


def sum_subest(s,k,r,w,x,m):
    x[k]==1
    if s+w[k]==m:
        print_solution(w,x)
    elif s+w[k]+s[w+1]<=m:
        sum_subest(s+w[k],k+1,r-w[k],w,x,m)
    if s+r-w[k]>=m and s+w[k+1]<=m:
        x[k]==0
        sum_subest(s,k+1,r-w[k],w,x,m)

def print_solution(w,x):
    subset=[w[i] for i in range(len(x)) if x[i]==1]
    print(f"the solution is {tuple(subset)}",end=" ")
    print(f"the vectorr is [",end=" ")
    for row in w:
        print("1" if  row in subset  else "0",end=" ")
        print("]")


def generate_subset(w,s):
    n=len(w)
    x=[0]*n
    r=sum(w)
    sum_subest(0,0,r,w,x,r)

def main():
    n=int(input("enter the elemenst"))
    w=[int(input(f"enter the elemens {i+1}"))for i in range(n)]
    s=int("enter thetarget")
    w.sort()
    generate_subset(w,s)
