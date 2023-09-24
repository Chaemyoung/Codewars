def accum(s):
    #Save final answer here
    final_word = ""
    
    # enumerate() do counts add number of the items on the list
    for index, word in enumerate(s):
        # make the first letter uppercase and rest lowercase
        final_word += word.upper() + word.lower()*index
        # Basically when it reachs the last letter, it stops adding - between letter because no needed
        if index != len(s) - 1:
            final_word += "-"
    return final_word
