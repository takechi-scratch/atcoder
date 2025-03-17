import time

before_good = False
for i in range(1, 10 ** 18):
    keta_sum = sum([int(x) for x in list(str(i))])
    print(f"{i} : {keta_sum} {i % keta_sum == 0}")

    time.sleep(0.01)
