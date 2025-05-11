S = input()
for x in S:
    if x.upper() == x:
        # こうすると改行を入れずに続けられる
        print(x, end="")

print("")
