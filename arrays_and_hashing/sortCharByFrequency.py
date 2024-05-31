def frequencySort(self, s: str) -> str:
    char_freq = {}
    for char in s:
        char_freq[char] = 1 + char_freq.get(char, 0)

    sorted_chars = sorted(char_freq, key=lambda x: char_freq[x], reverse=True)

    res = ''.join(char * char_freq[char] for char in sorted_chars)
    return res