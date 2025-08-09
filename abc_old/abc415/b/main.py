S = input()
positions = [i + 1 for i in range(len(S)) if S[i] == "#"]

for i in range(len(positions) // 2):
    print(positions[2 * i], positions[2 * i + 1], sep=",")
