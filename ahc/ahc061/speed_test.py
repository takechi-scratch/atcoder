import time

start = time.time()

import random

score = 0
x = 0.0
while time.time() - start < 2.0:
    score += 1
    x += random.random()

print(score)
