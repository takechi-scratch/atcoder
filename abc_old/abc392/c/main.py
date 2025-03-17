N = int(input())
P = [int(x) - 1 for x in input().split()]
Q = [int(x) - 1 for x in input().split()]
# 「そのゼッケンをつけているのはだれか」を先に記録
bib = [-1] * N
for i in range(N):
    bib[Q[i]] = i

for i in range(N):
    print(Q[P[bib[i]]] + 1, end=" ")
