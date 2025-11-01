# 尺取りでなんとかできないかとがんばってみた

N, A, B = [int(x) for x in input().split()]
S = list(input())
drives = [i + 1 for i, x in enumerate(S) if x == "a"]

left = -1
ans = 0
for right in range(len(drives)):
    while right - left >= A:
        days = drives[right] - drives[left + 1] + 1
        a_days = right - left
        b_days = days - a_days
        if b_days < B:
            # OKになった場合
            if left == -1:
                left_B_max = 0
            else:
                left_B_max = drives[left + 1] - drives[left] - 1

            if right == N - 1:
                right_B_max = max(0, N - drives[right])
            else:
                right_B_max = drives[right + 1] - drives[right] - 1

            extendable_days = B - b_days - 1
            repeats = min(extendable_days, left_B_max) + 1
            now_ans = repeats * (repeats + 1) // 2
            if repeats > right_B_max + 1:
                hides = repeats - right_B_max - 1
                now_ans -= hides * (hides + 1) // 2

            ans += now_ans

        left += 1

    else:
        continue


print(ans)
