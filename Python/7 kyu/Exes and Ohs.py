def xo(s):
    count_x = 0
    count_o = 0
    
    lower_s = s.lower()
    
    for letter in lower_s:
        if letter == "x":
            count_x += 1
        elif letter == "o":
            count_o += 1
    
    if count_x == count_o:
        return True
    else:
        return False
