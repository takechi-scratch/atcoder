N = int(input())

def solve():
    for i in range(2, 22):
        print(f"? {i}")
        if int(input()) == 1:
            print(f"! {i - 1}")


solve()
