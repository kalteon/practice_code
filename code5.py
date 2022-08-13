import collections


def group_anagrams(str: list[str]) -> list[str]:
    anagrams = collections.defaultdict(list)
    for word in str:
        anagrams[''.join(sorted(word))].append(word)
    return list(anagrams.values())

case = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(case))
