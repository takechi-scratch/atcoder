# floatとして受け取る（今回は小数の誤差は気にしなくてよかった）

X = float(input())
if X >= 38.0:
    print(1)
elif X >= 37.5:
    print(2)
else:
    print(3)
