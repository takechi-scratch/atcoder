A = [2, 3, 4, 5, 6]
ans = 0
while len(A) > 1:
    n1, n2 = A.pop(), A.pop()
    ans += n1 * n2
    A.append(n1 + n2)

print(ans)
