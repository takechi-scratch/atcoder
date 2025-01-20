S = input()
N = int(input())
K = [int(x) for x in input().split()]

def solve(pos):
    str_pos = (pos - 1) % len(S)
    hanten_pattern = bin((pos -1) // len(S))[2:]
    if hanten_pattern.count("1") % 2 == 0:
        return S[str_pos]
    else:
        return S[str_pos].swapcase()

print(*[solve(x) for x in K])
