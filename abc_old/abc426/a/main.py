ver = ["Ocelot", "Serval", "Lynx"]
X, Y = input().split()
print("Yes" if ver.index(X) >= ver.index(Y) else "No")
