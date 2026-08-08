X = "abc"
Y = "ab"

l = [X, Y]
for i in range(10):
    l.append(l[-1] + l[-2])

print(*l, sep="\n")
