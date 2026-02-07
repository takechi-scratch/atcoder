Q = int(input())
playing = 0
volume = 0
for _ in range(Q):
    i = int(input())
    if i == 1:
        volume += 1
    elif i == 2:
        volume = max(0, volume - 1)
    else:
        playing = 1 - playing

    print("Yes" if playing == 1 and volume >= 3 else "No")
