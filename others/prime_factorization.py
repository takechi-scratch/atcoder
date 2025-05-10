# UNIXコマンド"factor"を使った素因数分解
# windows環境では動きません。WSLなどを使ってください。

# > O(N ** 1/4)で50％以上の確率で素因数を発見することができます。
# https://qiita.com/t_fuki/items/7cd50de54d3c5d063b4a

import subprocess

def prime_factorization(x: int) -> list[int]:
    """素因数分解を行う関数

    Args:
        x (int): 素因数分解したい整数

    Returns:
        list[int]: 素因数分解した結果のリスト
    """

    out = subprocess.run(["factor", str(x)], stdout=subprocess.PIPE, check=True).stdout
    return [int(x) for x in out.decode().strip().split(" ")[1:]]



if __name__ == "__main__":
    # 使用例
    # Counterにそのまま突っ込めるので便利です
    from collections import Counter

    x = 100
    factors = Counter(prime_factorization(x))
    for factor, count in factors.items():
        print(f"{factor}: {count}")
