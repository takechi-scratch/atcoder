# 実際にシミュレートするしかない（ちょっと面倒）

A = [int(x) for x in input().split()]

for i in range(4):
    # copyしないとAの値が変わってしまうので注意
    a_temp = A.copy()

    # 入れ替える（そのために一時的に保存）
    temp = a_temp[i]
    a_temp[i] = a_temp[i + 1]
    a_temp[i + 1] = temp

    # 値の並びをチェック（1つでも前の値の方が大きくなっていたらアウト）
    for j in range(4):
        if a_temp[j] > a_temp[j + 1]:
            break

    else:
        print("Yes")
        break

else:
    print("No")
