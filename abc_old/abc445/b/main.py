N = int(input())
S = [input() for _ in range(N)]
max_len = len(max(S, key=lambda x: len(x)))

for x in S:
    count = (max_len - len(x)) // 2
    print("." * count + x + "." * count)
