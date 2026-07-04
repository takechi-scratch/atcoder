A = ["Sunny", "Cloudy", "Rainy"]
S = input()
print(A[(A.index(S) + 1) % 3])
