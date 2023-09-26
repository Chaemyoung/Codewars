def unique_in_order(sequence):
    list = []

    # If the list is empty, or the last item in the list isn't the same as the current letter, then append it to the list
    # So basically, there are repeatable letter, but we don't want to add multiple same letters, so we check the last letter of the list
    # Example, [a, b, c] If the next letter in the for loop is c again, then we don't add another c to the list. However, if the next one is d, it is not the same one right? then we include d in the list.
    for i in sequence:
        if len(list) == 0 or i != list[-1]:
            list.append(i)
            
    return list
