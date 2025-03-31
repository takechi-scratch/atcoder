N, M = [int(x) for x in input().split()]
S = input()
C = [int(x) - 1 for x in input().split()]
color_pos = [[] for _ in range(M)]
color_pos_pos = []

for i, x in enumerate(C):
    color_pos[x].append(i)
    color_pos_pos.append(len(color_pos[x]) - 1)

ans = []

for i in range(N):
    our_group = color_pos[C[i]]
    ans.append(S[our_group[(color_pos_pos[i] - 1) % len(our_group)]])

print("".join(ans))
