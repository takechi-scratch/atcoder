A, B = [int(x) for x in input().split()]
# A / B の切り上げはこれで求められる
print((A - 1) // B + 1)

# math.ceilだと誤差で無理でした！！！
