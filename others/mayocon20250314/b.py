N, M = [int(x) for x in input().split()]
things = [[int(x) for x in input().split()] for _ in range(N)]

for superior in range(N):
    sp_features = set(things[superior][2:])

    for inferior in range(N):
        if superior == inferior:
            continue

        if things[superior][0] > things[inferior][0]:
            continue

        for feature in things[inferior][2:]:
            if feature not in sp_features:
                break

        else:
            if things[superior][1] > things[inferior][1] or things[superior][0] < things[inferior][0]:
                print("Yes")
                exit()

print("No")
