N, M = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
# はじめにansを作っておいて、そこからAを引いていく
# rangeなので初めから昇順になっている
ans = list(range(1, N + 1))

for i in range(M):
    # removeをするときはリストの長さに比例した時間がかかるが、
    # 制約的に問題ない
    ans.remove(A[i])

print(len(ans))
# これでansをスペース区切りで出力できる！
print(*ans)
