X = int(input())
now = 100
year = 0
while now < X:
    now += now // 100
    year += 1

print(year)
