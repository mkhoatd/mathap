import math
A = [[4, 12, -16], [12, 37, -43], [-16, -43, 98]]
n = 3
L = [[0 for x in range(n+1)] for y in range(n+1)]

L[0][0]=math.sqrt(A[0][0])
L[1][0]=A[1][0]/L[0][0]
for i in range(n+1):
    for j in range(n+1):
        if i==j:
            L[i][j]=math.sqrt(A[i][j]-sum())
