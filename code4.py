import collections


def most_comman_word(paragraph: str, banned: list[str]) -> str:
    words = []
    paragraph = paragraph.lower()
    for char in paragraph:
        if char < 'a' or char > 'z':
            paragraph = paragraph.replace(char, ' ')
    for word in paragraph.split():
        if word != banned[0]:
            words.append(word)
    counts = collections.Counter(words)
    return counts.most_common(1)[0][0]

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
print(most_comman_word(paragraph, banned))
