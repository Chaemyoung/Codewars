def duplicate_encode(word):
    word = word.lower()
    count = {}
    result = ''

    for char in word:
        count[char] = count.get(char, 0) + 1

    for char in word:
        if count[char] > 1:
            result += ')'
        else:
            result += '('

    return result
