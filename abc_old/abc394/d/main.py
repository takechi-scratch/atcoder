S = list(input())

start = {"(", "[", "<"}
end = {")", "]", ">"}
pair = {"(": ")", "[": "]", "<": ">"}

stack = []
for i, x in enumerate(S):
    if x in start:
        stack.append(x)
    elif x in end:
        if len(stack) == 0 or x != pair[stack[-1]]:
            print("No")
            exit()

        stack.pop()

print("Yes" if len(stack) == 0 else "No")
