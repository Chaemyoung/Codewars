def get_count(sentence):
    sen_lower = sentence.lower()
    list = ['a', 'e', 'i', 'o', 'u']
    vowel_count = 0
    
    for word in sen_lower:
        if word.isalpha():
            if word in list:
                vowel_count += 1
            else: 
                pass
    return vowel_count
