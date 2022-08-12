def reverseString1(s) -> None:
    left, right = 0, len(s) -1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
def reverseString2(s) -> None:
    s.reverse

case = ["h", "e", "l", "l", "o"]
reverseString1(case)
print(case)
reverseString2(case)
print(case)