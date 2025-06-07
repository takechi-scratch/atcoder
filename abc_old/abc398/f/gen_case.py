from random import randint, choices

print(*choices("QWERTYUIOPASDFGHJKLZXCVBNM", k=randint(1, 20)), sep="")
