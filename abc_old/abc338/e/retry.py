# 解説見ずに再挑戦

N = int(input())
chords = [-1 for _ in range(2 * N)]
for _ in range(N):
    a, b = [int(x) - 1 for x in input().split()]
    chords[a] = b
    chords[b] = a

stack = []
stack_set = set()

for i in range(2 * N):
    if chords[i] in stack_set:
        if len(stack) <= 0 or stack.pop() != chords[i]:
            print("Yes")
            exit()
        stack_set.discard(chords[i])

    else:
        stack.append(i)
        stack_set.add(i)

if len(stack) > 0:
    print("Yes")
else:
    print("No")
