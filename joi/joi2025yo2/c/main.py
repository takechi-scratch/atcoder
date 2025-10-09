from bisect import bisect_right

X, Y, Z, P = [int(x) for x in input().split()]
A = list(set(int(x) for x in input().split()))
B = list(set(int(x) for x in input().split()))
C = list(set(int(x) for x in input().split()))

A.sort()
B.append(-(10**18))
B.append(10**18)
B.sort()

C.sort()
C = [C[0], C[-1]]
bob_target = P - (max(C) + min(C)) / 2


bob_worst = bob_target
for i, x in enumerate(A):
    k = bisect_right(B, bob_target - x)
    diff_1 = abs((bob_target - x) - B[k])
    diff_2 = abs((bob_target - x) - B[k - 1])
    if diff_1 < diff_2:
        bob_ans = x + B[k]
    else:
        bob_ans = x + B[k - 1]

    if abs(bob_worst - bob_target) < abs(bob_ans - bob_target):
        bob_worst = bob_ans

# WAポイント！JOIは必ず整数で出力すること。（"0.0"はNG）
# printの前にintをつけておいた方が無難。
print(int(max(abs(bob_worst + x - P) for x in C)))
