N, K = [int(x) for x in input().split()]
S = list(input())

for i in range(N):
    if S[i] == "o":
        if i < N - 1:
            S[i + 1] = "."
        if i > 0:
            S[i - 1] = "."

o_count = 0
hatena_combos = []
current_combo = 0
for i, x in enumerate(S):
    if x == "o":
        o_count += 1

    if x == "?":
        current_combo += 1
    elif current_combo > 0:
        hatena_combos.append(current_combo)
        current_combo = 0

if current_combo > 0:
    hatena_combos.append(current_combo)

limit = 0
for x in hatena_combos:
    limit += (x + 1) // 2

if K - o_count < 0:
    raise RuntimeError
elif K - o_count == 0:
    # それ以外.
    print("".join([x if x != "?" else "." for x in S]))
elif K - o_count < limit:
    # ?
    print(*S, sep="")
elif K - o_count == limit:
    # いい感じに埋める
    cur = 0
    now_combo = 0
    ans = []
    for i, x in enumerate(S):
        if x != "?":
            ans.append(x)
            if i > 0 and S[i - 1] == "?":
                cur += 1
                now_combo = 0
            continue

        if hatena_combos[cur] % 2 == 0:
            ans.append("?")
        else:
            ans.append("o" if now_combo % 2 == 0 else ".")

        now_combo += 1

    print(*ans, sep="")

else:
    raise RuntimeError
