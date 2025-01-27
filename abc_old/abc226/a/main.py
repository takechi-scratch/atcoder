# 直感的な四捨五入にはDecimalモジュールを
# 参考: https://note.nkmk.me/python-round-decimal-quantize/#decimalquantize

from decimal import Decimal, ROUND_HALF_UP
print(Decimal(input()).quantize(Decimal('0'), ROUND_HALF_UP))
