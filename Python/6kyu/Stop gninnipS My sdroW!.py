def spin_words(sentence):
    words = sentence.split()
    list = []
    
    for i in words:
        if len(i) >= 5:
            rotated_word = i[::-1]
            list.append(rotated_word)
        else:
            list.append(i)
    rotated_text = " ".join(list)
    return rotated_text
