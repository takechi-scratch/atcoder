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


from random import randrange

for _ in range(200000):
    prime_factorization(randrange(10**6, 10**7))
