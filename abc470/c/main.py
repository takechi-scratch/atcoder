# Codon動作確認済み

N, Q = [int(x) for x in input().split()]
A = [0] * N
nonzero = set()
ans = 0

for _ in range(Q):
    query = [int(x) for x in input().split()]
    if query[0] == 1:
        x = query[1] - 1
        ans ^= A[x]
        A[x] += 1
        ans ^= A[x]
        nonzero.add(x)
    else:
        for x in nonzero.copy():
            ans ^= A[x]
            A[x] -= 1
            ans ^= A[x]
            if A[x] == 0:
                nonzero.remove(x)

    print(ans)
