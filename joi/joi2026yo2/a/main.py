from bisect import bisect_left

N = int(input())
A = [int(x) for x in input().split()]
A.sort()

ans = -(10**18)
diff = 10**18

for high_least in sorted(list(set(A))):
    normals = bisect_left(A, high_least)
    highs = N - normals

    if abs(normals - highs) < diff or (abs(normals - highs) == diff and high_least > ans):
        ans = high_least
        diff = abs(normals - highs)

print(ans)
