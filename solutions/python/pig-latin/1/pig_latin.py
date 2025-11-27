vowels = "aeiou"


def add_ay(word: str) -> str:
    return word + "ay"


def word_translate(word: str) -> str:
    # We'll use the lowercase version for rule checks,
    # but build the result from the original word to preserve any casing.
    w = word.lower()

    # Rule 1: starts with vowel, or with "xr" or "yt"
    if w[0] in vowels or w.startswith("xr") or w.startswith("yt"):
        return add_ay(word)

    # Rule 3: zero or more consonants followed by "qu"
    # Only apply if *everything before "qu"* is consonants.
    for i in range(len(w) - 1):
        if w[i:i+2] == "qu" and all(ch not in vowels for ch in w[:i]):
            # move prefix (consonants + "qu") to the end
            prefix = word[:i+2]
            rest = word[i+2:]
            return rest + prefix + "ay"

    # Rule 4: one or more consonants followed by "y"
    # y must NOT be the first letter here.
    for i, ch in enumerate(w):
        if ch in vowels:
            break  # hit a vowel first → Rule 2 will handle it
        if ch == "y" and i > 0:
            # move consonants before 'y' to the end
            return word[i:] + word[:i] + "ay"

    # Rule 2: one or more consonants followed by a vowel
    i = 0
    while i < len(w) and w[i] not in vowels:
        i += 1
    # move leading consonant cluster to the end
    return word[i:] + word[:i] + "ay"


def translate(text: str) -> str:
    words = text.split()
    return " ".join(word_translate(w) for w in words)