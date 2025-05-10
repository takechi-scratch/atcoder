# Python用の安全なローリングハッシュを作りました！スライスでの取得に対応。

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


if __name__ == "__main__":
    print(f"{RollingHash.MOD = }")
    print(f"{RollingHash.B = }")

    str_a = "abcde"
    str_b = "cdeab"

    hash_a = RollingHash(str_a)
    hash_b = RollingHash(str_b)

    print(f"{hash_a.get() = }")
    print(f"{hash_a.get(0, 2) = }")
    print(f"{hash_a[0:2] = }")

    print(f"{hash_b.get(3, 5) = }")
    print(f"{hash_b[3:5] = }")
