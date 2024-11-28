# https://atcoder.jp/contests/abc322/tasks/abc322_c

N, M = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

# カーソルを作って、次の花火大会は何回目か保存。
# 花火大会の日をソートしておくべきだったかも
cur = 0
ans = []
for now in range(1, N+1):
    if A[cur] == now:
        ans.append("0")
        cur += 1
    else:
        ans.append(str(A[cur] - now))

print("\n".join(ans))
