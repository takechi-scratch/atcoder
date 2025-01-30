import time
from random import randint
from itertools import combinations

N = int(input("N > "))
test = [randint(0, 10 ** 9) for _ in range(16)]

start = time.time()

for _ in range(N):
    combinations(test, 2)

end = time.time()

print("completed!")
print(f"time: {end - start}")
