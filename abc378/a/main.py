A = [int(x) for x in input().split()]
ans = 0

for i in range(1, 5):
    # WAポイント！問題文をよく読むこと() count==4のときは2回分。
    ans += (A.count(i) >= 2) + (A.count(i) == 4)

print(ans)
