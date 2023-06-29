def consonant_count(s):
    con = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    con_num = 0
    word = s.lower()
    
    for letter in word:
        if letter.isalpha():
            if letter in con:
                con_num += 1
            else:
                pass
    return con_num
