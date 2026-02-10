# https://atcoder.jp/contests/abc240/tasks/abc240_d

N = int(input())
X = [int(x) for x in input().split()]

pipe = []
k = -1
cnt = 0

for i, a in enumerate(X):
    pipe.append(a)
    if k == a:
        cnt += 1
        if cnt >= k:
            del pipe[-1 * k:]

            # kとcntの再計算。二重ループになるかなと思ったけど、問題なさそう。
            if len(pipe) > 0:
                k = pipe[-1]
                cnt = 0
                for j in range(-1, - 1 - len(pipe), -1):
                    if pipe[j] == k:
                        cnt += 1
                    else:
                        break
            else:
                k = -1
                cnt = 0

    else:
        k = a
        cnt = 1

    print(len(pipe))
