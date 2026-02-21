seq = [3, 2]
while True:
    seq.append(seq[-1] * 1 + seq[-2] * 2)
    if seq[-1] % 4 == 0:
        break

print(seq)
