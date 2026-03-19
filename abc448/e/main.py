K, M = [int(x) for x in input().split()]
N = [[int(x) for x in input().split()] for _ in range(K)]

ANS_MOD = 10007

# 1を並べた時の商・あまり
divide_cache = [(0, 0)]
divide_cache_set = set([(0, 0)])
while True:
    q, m = divide_cache[-1]
    q *= 10
    m *= 10
    m += 1
    q += m // M
    q %= ANS_MOD
    m %= M

    divide_cache.append((q, m))
    if (q, m) in divide_cache_set:
        break
    divide_cache_set.add((q, m))

syuki_root = divide_cache.index(divide_cache[-1])
syuki = len(divide_cache) - syuki_root - 1


power_q = [0, 1]
for i in range(len(divide_cache + 1)):
    now = power_q[-1] * 10



def divide(repeat: int):
    if repeat < len(divide_cache):
        return divide_cache[repeat]

    return_pos = (repeat - syuki_root) % syuki + syuki_root
    return divide_cache[return_pos]


ans_q, ans_m_mod = 0, 0
power = 0
for c, l in reversed(N):
    q, mod = divide(l)
    ans_q += q * c * pow(10, power, ANS_MOD)
    ans_q %= ANS_MOD

    ans_m_mod += mod * c * pow(10, power, M)
    ans_q += ans_m_mod // M
    ans_m_mod %= M

    power = (power + l - syuki_root) % syuki + syuki_root

print((ans_q + ans_m_mod // M) % ANS_MOD)
