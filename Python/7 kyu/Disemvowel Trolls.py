def disemvowel(string_): 
    word = string_ 
    list = ['a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U'] 
    for letter in list: 
        word = word.replace(letter, "") 
    return word
