# それぞれの桁が大きい順に並べる。
# *でリストなどの要素を展開して関数に渡すことができ、sepで区切り文字をなくしている
A = [int(x) for x in input().split()]
print(*reversed(sorted(A)), sep="")
