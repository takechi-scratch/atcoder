import random

print(1)
S = random.choices("qwertyuiopasdfghjklzxcvbnm", k=random.randint(1, 10))
print(len(S))
print(*S, sep="")
