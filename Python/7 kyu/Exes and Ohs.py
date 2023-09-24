def xo(s):
    # Record number of x and o
    count_x = 0
    count_o = 0

    # Make the sentence lowercase
    lower_s = s.lower()

    # If you find letter x, add 1 to count_x, if find o, add 1 to count_o
    for letter in lower_s:
        if letter == "x":
            count_x += 1
        elif letter == "o":
            count_o += 1

    # If the counts are equal, return True, If they are diff, return False
    if count_x == count_o:
        return True
    else:
        return False


# return count_x == count_o
