import random
ti, tj, ai, aj = 0, 0, 0, 0
M, L = [random.randint(1, 5) for _ in range(2)]

t_sousa = [random.randint(1, 10) for _ in range(M)]
a_sousa = [random.randint(1, 10) for _ in range(L)]
N = max(sum(t_sousa), sum(a_sousa))
t_sousa[-1] += max(0, N - sum(t_sousa))
a_sousa[-1] += max(0, N - sum(a_sousa))

print(ti, tj, ai, aj)
print(N, M, L)
for x in t_sousa:
    print(random.choice(["U", "D", "L", "R"]), x)

for x in a_sousa:
    print(random.choice(["U", "D", "L", "R"]), x)
