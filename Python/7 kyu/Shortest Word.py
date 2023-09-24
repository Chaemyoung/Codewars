def find_short(s):
    # List of number of the word in s
    numbers = []
    
    # Create a list of the seperated words from s
    split = s.split()
    
    # Count the number of the length of the word, append to numbers list and repeat
    for w in split:
        length_w = len(w)
        numbers.append(length_w)
    
    # Find the lowest length of the word in the list and return
    lowest_number = min(numbers)
    return lowest_number
