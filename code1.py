def is_palindrome1(s: str) -> bool:
    strs = []
    for char in s:
       if char.isalnum():
            strs.append(char.lower())
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
          return False
    return True
def is_palindrome2(s: str) -> bool:
    s.lower()
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char)
    return strs == strs[::-1]
case = input()
print(is_palindrome1(case))
print(is_palindrome2(case))