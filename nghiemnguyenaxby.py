# ax+by=c
def gcdExtended(a, b):
    # Base Case
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcdExtended(b % a, a)
    x = y1 - (b//a) * x1
    y = x1
    return gcd, x, y


# 7x+11y=13
# a=7
# b=11
# c=13
a, b, c = 7, 11, 13
d, k, l = gcdExtended(a, b)
q = c//d
x = q*k
y = q*l
print(f"Nghiệm riêng: x={x}, y={y}")
print(f"Nghiệm tổng quát: x={x}+{b//d}*r, y={y}-{a//d}*r")
