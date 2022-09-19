from __future__ import annotations
import numpy as np
from rich import print


def transpose(a):
    return [[a[j][i] for j in range(len(a))] for i in range(len(a[0]))]


def det3x3(m: 'list[list[float]]') -> 'float':
    return m[0][0]*m[1][1]*m[2][2]+m[0][1]*m[1][2]*m[2][0]+m[0][2]*m[1][0]*m[2][1]-m[0][2]*m[1][1]*m[2][0]-m[0][1]*m[1][0]*m[2][2]-m[0][0]*m[1][2]*m[2][1]


def pow_matrix(m: 'list[list[float]]', n) -> 'list[list[float]]':
    return [[m[i][j]**n for j in range(len(m[0]))] for i in range(len(m))]


def det(m: 'list[list[float]]') -> 'float':
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]
    if len(m) == 3:
        return det3x3(m)
    else:
        return sum([(-1)**i*m[0][i]*det([m[j][:i]+m[j][i+1:] for j in range(1, len(m))]) for i in range(len(m))])


def trace(m: 'list[list[float]]') -> 'float':
    return sum([m[i][i] for i in range(len(m))])


def eigvalue3x3(m: 'list[list[float]]') -> 'list[float]':
    coeff1 = -1
    coeff2 = trace(m)
    # coeff3=-1/2*sum([])
    coeff3 = -det([[m[0][0], m[0][1]], [m[1][0], m[1][1]]]) -\
        det([[m[0][0], m[0][2]], [m[2][0], m[2][2]]]) -\
        det([[m[1][1], m[1][2]], [m[2][1], m[2][2]]])
    coeff4 = det(m)
    coeff = [coeff1, coeff2, coeff3, coeff4]
    return list(np.roots(coeff))


def eigvalue2x2(m: 'list[list[float]]') -> 'list[float]':
    coeff = [1, -(trace(m)), det(m)]
    return list(np.roots(coeff))


def eigenvalue(m: 'list[list[float]]') -> 'list[float]':
    if len(m) == 2:
        return eigvalue2x2(m)
    if len(m) == 3:
        return eigvalue3x3(m)
    else:
        raise NotImplementedError("not implemented yet")


def eigenvectors2x2(m: 'list[list[float]]') -> 'list[list[float]]':
    return [v1, v2]


def eigenvectors3x3(m: 'list[list[float]]') -> 'list[list[float]]':

    return [v1, v2, v3]


def eigenvectors(M: 'list[list[float]]') -> 'list[list[float]]':
    if len(M) == 2:
        return eigenvectors2x2(M)
    if len(M) == 3:
        return eigenvectors3x3(M)
    else:
        raise NotImplementedError("not implemented yet")


A = [[1.0, 3.0, 3.0], [2.0, 5.0, 5.0], [7.0, 5.0, 3.0]]

print("eigenvalue:", eigenvalue(A))
print("eigenvectors:", eigenvectors(A))


def mat_mul(A: 'list[list[float]]', B: 'list[list[float]]') -> 'list[list[float]]':
    return [[sum([A[i][k]*B[k][j] for k in range(len(A[0]))]) for j in range(len(B[0]))] for i in range(len(A))]
