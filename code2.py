def reverseString(s) -> None:
    left, right = 0, len(s) -1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

case = ["h", "e", "l", "l", "o"]
reverseString(case)
print(case)