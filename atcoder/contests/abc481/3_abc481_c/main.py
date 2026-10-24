Q = int(input())
bank_len = 0
bank = {}

for _ in range(Q):
    name = input()
    if name not in bank:
        bank[name] = bank_len + 1
        bank_len += 1

    print(bank[name])
