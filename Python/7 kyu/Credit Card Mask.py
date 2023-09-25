def maskify(cc):
    # If the length of the word is longer than 4, then...
    if len(cc) > 4:
        # Find the length of the given word and subtract 4 from it, add the add the same number of it with "#" and also add last for letter of the sentence
        new_word = "#" * (len(cc) - 4) + cc[-4:]
        return new_word
    # If the length of the word is lower than 5, then just return the given word 
    elif len(cc) < 5:
        return cc
    # If the given word is empty, then return ''
    else:
        return ''
