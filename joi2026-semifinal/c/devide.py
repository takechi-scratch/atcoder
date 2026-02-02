def div(now, last_max = None):
    if last_max is None:
        last_max = now
    if now < 0:
        return []
    if now == 0:
        return [[]]
    res = []
    for pick in range(1, last_max + 1):
        for next_res in div(now - pick, min(last_max, pick)):
            res.append([pick] + next_res)
    return res

print(div(3))
