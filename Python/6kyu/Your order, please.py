def order(sentence):
    if not sentence:
        return ""

    words = sentence.split()
    sorted_words = sorted(words, key=lambda word: int(''.join(filter(str.isdigit, word))))
    sorted_sentence = ' '.join(sorted_words)
    return sorted_sentence
