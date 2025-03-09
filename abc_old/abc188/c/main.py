N = int(input())
A = [int(x) for x in input().split()]

battle_team = list(range(2 ** N))

for _ in range(N - 1):
    next_team = []
    for i in range(0, len(battle_team), 2):
        # print(i)
        if A[battle_team[i]] < A[battle_team[i + 1]]:
            next_team.append(battle_team[i + 1])
        else:
            next_team.append(battle_team[i])

    battle_team = next_team

if A[battle_team[0]] < A[battle_team[1]]:
    print(battle_team[0] + 1)
else:
    print(battle_team[1] + 1)
