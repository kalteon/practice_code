def longest_palindrome(s: str) -> str:
    if len(s) < 2 or s == s[::-1]:
        return s
    result = ""
    for i in range(len(s) - 1):
        result = max(result, expand(i, i+1, s), expand(i, i+2, s), key=len)
    return result
def expand(left, right, s) -> str:
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left + 1: right]

case = input()
print(longest_palindrome(case))
