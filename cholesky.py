import math
from rich import print
A = [[4, 12, -16], [12, 37, -43], [-16, -43, 98]]
n = 3
L = [[0 for x in range(n)] for y in range(n)]
print("A=", A)
print("n=", n)
print("L=", L)
for j in range(n):
    for i in range(j,n):
        print("i=", i, "j=", j)
        print("before: L[i][j]=", L[i][j])
        if i==j:
            suml=sum([L[i][k]*L[i][k] for k in range(j)])
            L[i][j]=math.sqrt(A[i][j]-suml)
        else:
            print(f"log L[{j}][{j}]=", L[j][j])
            L[i][j]=1/L[j][j]*(A[i][j]-sum([L[i][k]*L[j][k] for k in range(j)]))
        print("after: L[i][j]=", L[i][j])
        print("\n\n")

print(L)