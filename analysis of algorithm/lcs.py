def lcs(X,Y):
    m=len(X)
    n=len(Y)

    c=[[0]*(n+1) for _ in range(m+1)]

    for i in range(1,m+1):
        for j in range(1,n+1):
            if X[i-1]==Y[j-1]:
                c[i][j]=c[i-1][j-1]+1
            else:
                c[i][j]=max(c[i-1][j],c[i][j-1])


    length=c[m][n]
    lcs=[]
    i=m
    j=n
    while i>0 and j>0:
       if X[i-1]==Y[j-1]:
           lcs.append(X[i-1])
           
           j-=1
           i-=1
       elif c[i-1][j]>c[i][j-1]:
           i-=1
       else:
           j-=1
    lcs.reverse()
    print("dyanmic matrix")
    for row in c:
        print(''.join(map(str,row)))
    return length,''.join(lcs) 


if __name__=="__main__":
    X=input("ENTER THE FIRST SEQENCE")
    Y=input("ENTER THE SECOND SEQENCE")

    length,lcs=lcs(X,Y)
    print("LENGTH OF LCS IS",length)
    print("longest common ",lcs)


def Lcs(X,Y):
    m=len(X)
    n=len(Y)
    c=[[0]*(n+1) for _ in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if X[i-1]==Y[j-1]:
                c[i][j]=c[i-1][j-1]+1
            else:
                c[i][j]=max(c[i-1][j],c[i][j-1])

    lcs=[]
    i=m
    j=n
    length=c[m][n]

    while i>0 and j>0:
        if X[i-1]==Y[j-1]:
            lcs.append(X[i-1])
            i-=1
            j-=1
        elif c[i-1][j]>=c[i][j-1]:
            i-=1
        else:
            j-=1
    lcs.reverse()

    print("dyanmaiv ")
    for row in c:
        print(''.join(map(str,row)))

    return length,''.join(lcs)

if __name__=="__main__":
    X=input("ENTER THE FIRST SEQENCE")
    Y=input("ENTER THE SECOND SEQENCE")

    length,lcs=Lcs(X,Y)
    print("LENGTH OF LCS IS",length)
    print("longest common ",lcs)

