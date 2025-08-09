S = input()
bef = False
if S.count("#") == 0:
  print("o" + "."*(len(S)-1))
  exit()

S += "#"

for i, x in enumerate(S):
  if i == len(S) -1:
    break

  if x =="#":
    print("#", end="")
  elif i < len(S) - 1 and S[i+1]=="#":
    print("o", end="")
  else:
    print(".", end="")


print("")
