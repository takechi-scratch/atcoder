#https://qiita.com/embermaverick05/items/93b7258436c55b4a0528

class BIT:
    def init(self, N):
        self.N = N
        self.bits = [0] * (self.N + 1)

    def update(self, i, x):
        while i <= self.N:
            self.bits[i] += x
            i += i & -i

    def total(self, i):
        res = 0

        while i > 0:
            res += self.bits[i]
            i -= i & -i

        return res

N = int(input())
N = N*2
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A = sorted(A)+sorted(B)
bits = BIT(N)

count = 0

for i in range(N - 1, -1, -1):
    count += bits.total(A[i] - 1)
    bits.update(A[i], 1)

print(count)
