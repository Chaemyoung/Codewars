def get_middle(s):
      ###return s[(len(s)-1)//2:(len(s)+2)//2]

    if len(s) == 0:
        return ''
    elif len(s) == 1:
        return s
    elif len(s) == 2:
        return s
    elif (len(s) % 2) == 0:
        return s[(len(s)-1)//2:(len(s)+2)//2]
    else:
        return s[len(s) // 2]
