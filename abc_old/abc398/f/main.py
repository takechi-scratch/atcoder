import random

class RollingHash:
    """safe, fast rolling Hash for string matching.
    Reference:
    - https://kyoroid.github.io/algorithm/string/rolling_hash.html
    - https://qiita.com/keymoon/items/11fac5627672a6d6a9f6
    """
    MOD = (1 << 61) - 1
    B = random.randint(2, 1 << 15)

    MASK30 = (1 << 30) - 1
    MASK31 = (1 << 31) - 1
    MASK61 = MOD

    def __init__(self, S: str):
        """Initializes the rolling hash object for a given string. O(N)

        Args:
            S (str): The input string for which the rolling hash will be computed.
        Attributes:
            n (int): The length of the input string.
            prefix (List[int]): The prefix hash values for the input string.
            power (List[int]): The precomputed powers of the base value modulo `m`.
        """

        self.n = n = len(S)
        self.prefix = prefix = [0] * (n + 1)
        self.power = power = [1] * (n + 1)
        b = RollingHash.B
        for i in range(n):
            c = ord(S[i])
            prefix[i + 1] = self._mod(self._multiply(prefix[i], b) + c)
            power[i + 1] = self._mod(self._multiply(power[i], b))

    def get(self, l: int = 0, r: int = 0) -> int:
        """Returnss the hash value of the substring S[l:r]. O(1)"""
        if r <= 0: r += self.n
        if not 0 <= l < r <= self.n:
            raise IndexError("index out of range")

        return self._mod(self.prefix[r] - self._multiply(self.power[r - l], self.prefix[l]))

    def _multiply(self, a: int, b: int) -> int:
        """Multiplies two numbers under modulo."""
        au = a >> 31
        ad = a & RollingHash.MASK31
        bu = b >> 31
        bd = b & RollingHash.MASK31
        mid = ad * bu + au * bd
        midu = mid >> 30
        midd = mid & RollingHash.MASK30
        return au * bu * 2 + midu + (midd << 31) + ad * bd

    def _mod(self, x: int) -> int:
        """Calculates the modulo of a number."""
        xu = x >> 61
        xd = x & RollingHash.MASK61
        res = xu + xd
        if res >= RollingHash.MOD:
            res -= RollingHash.MOD
        return res

    def __getitem__(self, item):
        if not isinstance(item, (slice, int)):
            raise TypeError("index must be int or slice")

        if isinstance(item, int):
            if item < 0:
                item += self.n
            if not 0 <= item < self.n:
                raise IndexError("index out of range")
            return self.prefix[item]

        if item.step is not None:
            raise ValueError("this can't be set step")

        return self.get(item.start, item.stop)

S = input()

if len(S) == 1:
    print(S)
    exit()

# テンプレコード、接頭辞・接尾辞の回文判定
# あらかじめ逆さのロリハを作っておけばすぐできる
S_hash = RollingHash(S)
reversed_S_hash = RollingHash(S[::-1])

# 回文全体の長さでループ。短い方から試してOKなら終了
for palindrome_len in range(len(S), len(S) * 2):
    self_must = (len(S) + 1) // 2 - (palindrome_len - len(S) + 1) // 2
    center = palindrome_len // 2
    check_len = len(S) - center

    if S_hash[center - check_len + (palindrome_len % 2 == 1): center + (palindrome_len % 2 == 1)] == reversed_S_hash[0 : len(S) - center]:
        plus_str = S[0:palindrome_len - len(S)]
        print(S + plus_str[::-1])
        break

else:
    raise RuntimeError
