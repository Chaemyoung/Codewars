def is_isogram(string):
    word = string.lower()
    
    list = []
    for letter in word:
        if letter.isalpha():
            if letter in list:
                return False
            else:
                list.append(letter)

    return True

###Got the idea from here https://www.geeksforgeeks.org/check-string-isogram-not/
