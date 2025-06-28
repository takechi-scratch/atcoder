import itertools
import more_itertools

def divide_group(N: int):
    """N未満の非負整数をグループ分けするとき、考えられる組み合わせを列挙
       N<=5のときしか使い物にならない

    Args:
        N (int): 要素の数

    """

    d = list(range(N))
    l = list(more_itertools.powerset(d))[1:]

    for i in range(1, N + 1):
        for ans in itertools.combinations(l, i):
            check = []
            for x in ans:
                check.extend(x)

            if len(check) == N and sorted(check) == d:
                yield ans

if __name__ == "__main__":
    N = 5
    for x in divide_group(N):
        print(x)
